from typing import Dict, Union, Any
from promptfoo_customizations.types.promptfoo.assertions import AssertionValueFunctionContext, GradingResult
from promptfoo_customizations.providers import owui
from promptfoo_customizations.providers.utils import read_owui_yaml_provider_config
from pathlib import Path
import json

# TODO: Move to external j2 file or at least handle better the substitution in last list item
PROMPT = [
  {
    "role": "system",
    "content": "Du vurderer om givne svar er bekræftende eller afvisende i forhold et spørgsmål. Giv en numerisk score fra -10 (helt klar afvisning) over 0 (neutral) til 10 (helt klar bekræftelse). Svar i JSON format: {\"reason\": \"string\", \"category\": enum [\"Bekræftende\", \"Neutralt\", \"Afvisende\"], \"score\": number}. ALLE begrundelser skal være på dansk."
  },
  {
    "role": "user",
    "content": """<Spørgsmål>
    vedr. klasselister til kommende skolestarter. 
    Må vi skrive forældrenes telefon nr på listerne?
    </Spørgsmål>
    
    <Svar>
    Klasselister til kommende skolestarter må kun indeholde elevers fulde navn.
    </Svar>
    """
  },
  {
    "role": "assistant",
    "content": "{\"reason\": \"Svaret fortæller meget explicit, at klasselister kun må indeholde fulde navn, hvilket udelukker alle former for telefon numre. Svaret kunne dog have svaret meget mere direkte på det faktiske spørgsmål, det er derfor en relativ vag afvisning.\", \"category\": \"Afvisende\", \"score\": -3}"
  },
  {
    "role": "user",
    "content": """<Spørgsmål>
    Må vi gerne have en elev, der har svært ved at komme i skole med på fjernundervisning, så eleven kan følge med i det vi laver fx. via google meet?
    </Spørgsmål>
    
    <Svar>
    Ja, en elev må gerne følge undervisningen via et videolink, som for eksempel med Google Meet. Ifølge retningslinjer skal du være opmærksom på at der ikke transmitteres noget af følsomt eller fortroligt karakter.
    </Svar>
    """
  },
  {
    "role": "assistant",
    "content": "{\"reason\": \"Svaret formidler klart og tydeligt at det er tilladt\", \"category\": \"Bekræftende\", \"score\": 10}"
  },
  {
    "role": "user",
    "content": """<Spørgsmål>
    Jeg vil gerne bruge billeder af børn fra skolegården på forsiden af skolens hjemmeside, må jeg det?
    </Spørgsmål>
    
    <Svar>
    I design af hjemmesider skal man være opmærksom på at billeder uden personer giver en dårligere bruger oplevelse, da det gør det sværere for børn, forældre og andre besøgende at relaterer til skolens aktiviteter og tilbud.
    </Svar>
    """
  },
  {
    "role": "assistant",
    "content": "{\"reason\": \"Svaret oplyser kun om brug af billeder i forhold til ux og giver ikke et direkte svar på spørgsmålet\", \"category\": \"Neutralt\", \"score\": 0}"
  },
  {
    "role": "user",
    "content": "<Spørgsmål>\n{question}\n</Spørgsmål>\n\n<Svar>\n{output}\n</Svar>"
  }
]

# Default function name
def get_assert(output: str, context: AssertionValueFunctionContext) -> GradingResult | Union[bool, float, Dict[str, Any]]:
    answer_category = context['config'].get('expectedAnswerCategory','Bekræftende').lower()
    # We discriminate categories on first character, just to minimize possible token errors
    category_discriminator = answer_category[0]
    positive_cat_discriminator = 'b'

    # Logging info
    print(f"[{Path(__file__).name}] Assert via llm as judge whether an answer is \"{answer_category}\" (category)")
    print(f"[{Path(__file__).name}] The variables provided variables: {context['vars']}")

    # Test provider specification falls back to the provider defined in defaultTest
    test_provider_specification = context.get('test',{}).get('options',{}).get('provider',{})
    provider_config = test_provider_specification.get('config',{})
    prompt = PROMPT
    prompt[-1]['content'] = PROMPT[-1]['content'].format(question=context['vars']['question'], output=output)
    result = owui.call(json.dumps(prompt), **read_owui_yaml_provider_config(provider_config))

    print(f"[{Path(__file__).name}] Judge model: {provider_config.get('model', None)}")

    result = json.loads(result['output'])
    if result['category'].lower().startswith(category_discriminator):
        passing = True
    else:
        passing = False
    # This return is an example GradingResult dict
    return {
      'pass': passing,
      'score': int((result['score'] if answer_category.startswith(positive_cat_discriminator) else abs(result['score'])) if passing else 0)/10,
      'reason': result['reason'],
    }