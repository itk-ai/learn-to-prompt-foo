"""
We need to check claims or informations are present in a piece of text / an answer.

All these claims should be categorisered into providing guidiance in regards to a question, or fill/courtous remark, general information

See approaches in https://github.com/promptfoo/promptfoo/blob/main/src/external/prompts/ragas.ts
"""
from typing import Dict, Union, Any
from promptfoo_customizations.types.promptfoo.assertions import AssertionValueFunctionContext, GradingResult
from promptfoo_customizations.prompt_templates.essential_claims import prompt_template
from promptfoo_customizations.clean_output import sanitize
from promptfoo_customizations.providers import owui
from promptfoo_customizations.providers.utils import read_owui_yaml_provider_config
from pathlib import Path
import json

# Default function name
def get_assert(output: str, context: AssertionValueFunctionContext) -> GradingResult | Union[bool, float, Dict[str, Any]]:
    essential_claims = context['config'].get('essentialClaims',[])

    # Logging info
    print(f"[{Path(__file__).name}] Assert via llm as judge whether a provided number of essential claims are covered in an answer")
    print(f"[{Path(__file__).name}] The essential claims provided: {essential_claims}")
    print(f"[{Path(__file__).name}] The variables provided: {context['vars']}")

    question = context['vars'].get('question')
    # Test provider specification falls back to the provider defined in defaultTest
    test_provider_specification = context.get('test',{}).get('options',{}).get('provider',{})
    provider_config = test_provider_specification.get('config', {})

    print(f"[{Path(__file__).name}] judge model: {provider_config.get('model', None)}")

    prompt = prompt_template.format(question=question, claims=essential_claims, answer=output)
    result = owui.call(json.dumps(prompt), **read_owui_yaml_provider_config(provider_config))
    result = json.loads(result['output'])

    return sanitize(result)