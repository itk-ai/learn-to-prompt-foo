class OWUIProvider {
  constructor(options) {
    this.config = options.config || {};

    if (!this.config.apiEndpointEnvironmentVariable) {
      throw new Error('Missing required config: apiEndpointEnvironmentVariable must be set');
    }

    if (!this.config.apiKeyEnvironmentVariable) {
      throw new Error('Missing required config: apiKeyEnvironmentVariable must be set');
    }

    if (!this.config.model) {
      throw new Error('Missing required config: model must be set');
    }

    if (this.config.outputSources === undefined) {
      throw new Error('Missing required config: outputSources must be set (true or false)');
    }
  }

  id() {
    return `owui:${this.config.apiEndpointEnvironmentVariable.toLowerCase()}:${this.config.model}`;
  }

  async callApi(prompt, context, options) {
    if (context?.logger) {
      context.logger.debug('OWUI Provider called', {
        promptLength: prompt.length,
        model: this.config.model,
        outputSources: this.config.outputSources,
      });
    }

    const endpointVariable = this.config.apiEndpointEnvironmentVariable;
    const endpoint = process.env[endpointVariable];

    if (!endpoint) {
      if (context?.logger) {
        context.logger.error(`Missing environment variable: ${endpointVariable}`);
      }
      return {
        error: `Missing environment variable: ${endpointVariable}`,
      };
    }

    const apiKeyVariable = this.config.apiKeyEnvironmentVariable;
    const apiKey = process.env[apiKeyVariable];

    if (!apiKey) {
      if (context?.logger) {
        context.logger.error(`Missing environment variable: ${apiKeyVariable}`);
      }
      return {
        error: `Missing environment variable: ${apiKeyVariable}`,
      };
    }

    let messages;
    try {
      messages = JSON.parse(prompt);
      if (context?.logger) {
        context.logger.debug('Parsed prompt as JSON messages', { messageCount: messages.length });
      }
    } catch (err) {
      if (context?.logger) {
        context.logger.debug('Using prompt as single user message');
      }
      messages = [{ role: 'user', content: prompt }];
    }

    const body = {
      messages: messages,
      model: this.config.model,
    };

    if (this.config.features) {
      body.features = this.config.features;
    }

    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify(body),
    });

    if (context?.logger) {
      context.logger.debug('OWUI API request', {
        endpoint,
        method: 'POST',
        requestBody: JSON.stringify(body),
      });
    }

    if (!response.ok) {
      const errorText = await response.text();
      if (context?.logger) {
        context.logger.error('OWUI API error', {
          status: response.status,
          statusText: response.statusText,
          error: errorText,
        });
      }
      return {
        error: `HTTP ${response.status}: ${errorText}`,
      };
    }

    const json = await response.json();

    if (context?.logger) {
      context.logger.debug('OWUI API response', json);
    }

    const text = json.choices?.[0]?.message?.content ?? null;
    if (text === null) {
      const error = 'Invalid response from API: missing "choices"';
      if (context?.logger) {
        context.logger.error(error);
      }
      return { error };
    }

    const output = { text };

    if (this.config.outputSources) {
      const metadata = json.sources?.[0]?.metadata;
      const sourcesContent = json.sources?.[0]?.document;

      output.sources = [];
      if (Array.isArray(metadata) && metadata.length > 0 && Array.isArray(sourcesContent) && sourcesContent.length == metadata.length) {
        output.sources = metadata.map((entry, index) => ({
          reference: entry?.source ?? null,
          content: sourcesContent[index]
        }));
        if (context?.logger) {
          context.logger.debug('Included sources in output', {
            sourceCount: output.sources.length,
          });
        }
      }
    }

    return { output };
  }
}

module.exports = OWUIProvider;
