{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "279b1418-560e-4fed-99ce-563600ccada8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: transformers in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (5.10.2)\n",
      "Requirement already satisfied: torch in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (2.12.0)\n",
      "Requirement already satisfied: pandas in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (3.0.3)\n",
      "Requirement already satisfied: sentencepiece in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (0.2.1)\n",
      "Requirement already satisfied: accelerate in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (1.13.0)\n",
      "Requirement already satisfied: huggingface-hub<2.0,>=1.5.0 in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (1.14.0)\n",
      "Requirement already satisfied: numpy>=1.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from transformers) (2.3.5)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from transformers) (25.0)\n",
      "Requirement already satisfied: pyyaml>=5.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from transformers) (6.0.3)\n",
      "Requirement already satisfied: regex>=2025.10.22 in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (2026.5.9)\n",
      "Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (0.22.2)\n",
      "Requirement already satisfied: typer in c:\\programdata\\anaconda3\\lib\\site-packages (from transformers) (0.20.0)\n",
      "Requirement already satisfied: safetensors>=0.4.3 in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (from transformers) (0.7.0)\n",
      "Requirement already satisfied: tqdm>=4.27 in c:\\programdata\\anaconda3\\lib\\site-packages (from transformers) (4.67.1)\n",
      "Requirement already satisfied: filelock>=3.10.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (3.20.0)\n",
      "Requirement already satisfied: fsspec>=2023.5.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (2025.10.0)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in c:\\users\\win11-pro\\appdata\\roaming\\python\\python313\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (1.5.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (0.28.1)\n",
      "Requirement already satisfied: typing-extensions>=4.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from huggingface-hub<2.0,>=1.5.0->transformers) (4.15.0)\n",
      "Requirement already satisfied: anyio in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (4.10.0)\n",
      "Requirement already satisfied: certifi in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (2026.4.22)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (3.11)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\programdata\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (0.16.0)\n",
      "Requirement already satisfied: setuptools<82 in c:\\programdata\\anaconda3\\lib\\site-packages (from torch) (80.9.0)\n",
      "Requirement already satisfied: sympy>=1.13.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from torch) (1.14.0)\n",
      "Requirement already satisfied: networkx>=2.5.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from torch) (3.5)\n",
      "Requirement already satisfied: jinja2 in c:\\programdata\\anaconda3\\lib\\site-packages (from torch) (3.1.6)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: tzdata in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: psutil in c:\\programdata\\anaconda3\\lib\\site-packages (from accelerate) (7.0.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from sympy>=1.13.3->torch) (1.3.0)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from tqdm>=4.27->transformers) (0.4.6)\n",
      "Requirement already satisfied: click>=8.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from typer->transformers) (8.2.1)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from typer->transformers) (1.5.4)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from typer->transformers) (14.2.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich>=10.11.0->typer->transformers) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich>=10.11.0->typer->transformers) (2.19.2)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer->transformers) (0.1.2)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from anyio->httpx<1,>=0.23.0->huggingface-hub<2.0,>=1.5.0->transformers) (1.3.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jinja2->torch) (3.0.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install -U transformers torch pandas sentencepiece accelerate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d167f900-bb0f-4896-a413-3e07732615b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['ticket_id', 'day_of_week', 'day_of_week_num', 'company_id',\n",
      "       'company_size', 'company_size_cat', 'industry', 'industry_cat',\n",
      "       'customer_tier', 'customer_tier_cat', 'org_users', 'region',\n",
      "       'region_cat', 'past_30d_tickets', 'past_90d_incidents', 'product_area',\n",
      "       'product_area_cat', 'booking_channel', 'booking_channel_cat',\n",
      "       'reported_by_role', 'reported_by_role_cat', 'customers_affected',\n",
      "       'error_rate_pct', 'downtime_min', 'payment_impact_flag',\n",
      "       'security_incident_flag', 'data_loss_flag', 'has_runbook',\n",
      "       'customer_sentiment', 'customer_sentiment_cat', 'description_length',\n",
      "       'priority', 'priority_cat'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"Support_tickets.csv\")\n",
    "\n",
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "979110c6-4bcc-4f59-8631-65ccb1afb57d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Possible text columns: ['day_of_week', 'company_size', 'industry', 'customer_tier', 'region', 'product_area', 'booking_channel', 'reported_by_role', 'customer_sentiment', 'priority']\n"
     ]
    }
   ],
   "source": [
    "text_columns = [col for col in df.columns if df[col].dtype == \"object\"]\n",
    "\n",
    "print(\"Possible text columns:\", text_columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9cf39943-dc26-438a-bade-1d96bfc6d35b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Selected text column: product_area\n"
     ]
    }
   ],
   "source": [
    "possible_cols = [col for col in df.columns if df[col].dtype == \"object\"]\n",
    "\n",
    "# pick the column with longest average text length\n",
    "text_col = max(possible_cols, key=lambda c: df[c].astype(str).str.len().mean())\n",
    "\n",
    "print(\"Selected text column:\", text_col)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e62d1874-3164-492b-bee7-48c0b971e679",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mobile\n"
     ]
    }
   ],
   "source": [
    "ticket = df[text_col].iloc[0]\n",
    "print(ticket)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2a381e69-300b-4ee5-899e-dd1fb3157f34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6b825dfc4ef64f8a85f19d060a7f3c78",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Loading weights:   0%|          | 0/282 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[transformers] The tied weights mapping and config for this model specifies to tie shared.weight to lm_head.weight, but both are present in the checkpoints with different values, so we will NOT tie them. You should update the config with `tie_word_embeddings=False` to silence this warning.\n",
      "[transformers] The model 'T5ForConditionalGeneration' is not supported for text-generation. Supported models are ['PeftModelForCausalLM', 'AfmoeForCausalLM', 'ApertusForCausalLM', 'ArceeForCausalLM', 'AriaTextForCausalLM', 'BambaForCausalLM', 'BartForCausalLM', 'BertLMHeadModel', 'BertGenerationDecoder', 'BigBirdForCausalLM', 'BigBirdPegasusForCausalLM', 'BioGptForCausalLM', 'BitNetForCausalLM', 'BlenderbotForCausalLM', 'BlenderbotSmallForCausalLM', 'BloomForCausalLM', 'BltForCausalLM', 'CamembertForCausalLM', 'CodeGenForCausalLM', 'CohereForCausalLM', 'Cohere2ForCausalLM', 'Cohere2MoeForCausalLM', 'CpmAntForCausalLM', 'CTRLLMHeadModel', 'CwmForCausalLM', 'Data2VecTextForCausalLM', 'DbrxForCausalLM', 'DeepseekV2ForCausalLM', 'DeepseekV3ForCausalLM', 'DeepseekV4ForCausalLM', 'DiffLlamaForCausalLM', 'DogeForCausalLM', 'Dots1ForCausalLM', 'ElectraForCausalLM', 'Emu3ForCausalLM', 'ErnieForCausalLM', 'Ernie4_5ForCausalLM', 'Ernie4_5_MoeForCausalLM', 'Exaone4ForCausalLM', 'ExaoneMoeForCausalLM', 'FalconForCausalLM', 'FalconH1ForCausalLM', 'FalconMambaForCausalLM', 'FlexOlmoForCausalLM', 'FuyuForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'Gemma3ForConditionalGeneration', 'Gemma3ForCausalLM', 'Gemma3nForConditionalGeneration', 'Gemma3nForCausalLM', 'Gemma4ForConditionalGeneration', 'Gemma4AssistantForCausalLM', 'Gemma4ForCausalLM', 'Gemma4UnifiedForConditionalGeneration', 'Gemma4UnifiedAssistantForCausalLM', 'Gemma4UnifiedForCausalLM', 'GitForCausalLM', 'GlmForCausalLM', 'Glm4ForCausalLM', 'Glm4MoeForCausalLM', 'Glm4MoeLiteForCausalLM', 'GlmMoeDsaForCausalLM', 'GotOcr2ForConditionalGeneration', 'GPT2LMHeadModel', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTNeoForCausalLM', 'GPTNeoXForCausalLM', 'GPTNeoXJapaneseForCausalLM', 'GptOssForCausalLM', 'GPTJForCausalLM', 'GraniteForCausalLM', 'GraniteMoeForCausalLM', 'GraniteMoeHybridForCausalLM', 'GraniteMoeSharedForCausalLM', 'HeliumForCausalLM', 'HrmTextForCausalLM', 'HunYuanDenseV1ForCausalLM', 'HunYuanMoEV1ForCausalLM', 'HYV3ForCausalLM', 'HyperCLOVAXForCausalLM', 'Jais2ForCausalLM', 'JambaForCausalLM', 'JetMoeForCausalLM', 'LagunaForCausalLM', 'Lfm2ForCausalLM', 'Lfm2MoeForCausalLM', 'LlamaForCausalLM', 'Llama4ForCausalLM', 'Llama4ForCausalLM', 'LongcatFlashForCausalLM', 'MambaForCausalLM', 'Mamba2ForCausalLM', 'MarianForCausalLM', 'MBartForCausalLM', 'MegatronBertForCausalLM', 'MellumForCausalLM', 'MiniMaxForCausalLM', 'MiniMaxM2ForCausalLM', 'MinistralForCausalLM', 'Ministral3ForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'MllamaForCausalLM', 'ModernBertDecoderForCausalLM', 'MoshiForCausalLM', 'MptForCausalLM', 'MusicgenForCausalLM', 'MusicgenMelodyForCausalLM', 'MvpForCausalLM', 'NanoChatForCausalLM', 'NemotronForCausalLM', 'NemotronHForCausalLM', 'OlmoForCausalLM', 'Olmo2ForCausalLM', 'Olmo3ForCausalLM', 'OlmoHybridForCausalLM', 'OlmoeForCausalLM', 'OpenAIGPTLMHeadModel', 'OPTForCausalLM', 'PegasusForCausalLM', 'PersimmonForCausalLM', 'PhiForCausalLM', 'Phi3ForCausalLM', 'Phi4MultimodalForCausalLM', 'PhimoeForCausalLM', 'PLBartForCausalLM', 'ProphetNetForCausalLM', 'Qwen2ForCausalLM', 'Qwen2MoeForCausalLM', 'Qwen3ForCausalLM', 'Qwen3_5ForCausalLM', 'Qwen3_5MoeForCausalLM', 'Qwen3_5MoeForCausalLM', 'Qwen3_5ForCausalLM', 'Qwen3MoeForCausalLM', 'Qwen3NextForCausalLM', 'RecurrentGemmaForCausalLM', 'ReformerModelWithLMHead', 'RemBertForCausalLM', 'RobertaForCausalLM', 'RobertaPreLayerNormForCausalLM', 'RoCBertForCausalLM', 'RoFormerForCausalLM', 'RwkvForCausalLM', 'SeedOssForCausalLM', 'SmolLM3ForCausalLM', 'SolarOpenForCausalLM', 'StableLmForCausalLM', 'Starcoder2ForCausalLM', 'TrOCRForCausalLM', 'VaultGemmaForCausalLM', 'WhisperForCausalLM', 'XGLMForCausalLM', 'XLMWithLMHeadModel', 'XLMRobertaForCausalLM', 'XLMRobertaXLForCausalLM', 'XLNetLMHeadModel', 'xLSTMForCausalLM', 'XmodForCausalLM', 'YoutuForCausalLM', 'ZambaForCausalLM', 'Zamba2ForCausalLM'].\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "generator = pipeline(\n",
    "    \"text-generation\",\n",
    "    model=\"google/flan-t5-base\"\n",
    ")\n",
    "\n",
    "def create_prompt(ticket):\n",
    "    return f\"\"\"\n",
    "You are a support ticket classifier.\n",
    "\n",
    "Ticket: {ticket}\n",
    "\n",
    "Return only one label (Billing, Technical, Account, General).\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "17a2a738-2448-48f0-ab3e-b1c269b7069a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[transformers] Passing `generation_config` together with generation-related arguments=({'do_sample', 'max_new_tokens'}) is deprecated and will be removed in future versions. Please pass either a `generation_config` object OR all generation parameters explicitly, but not both.\n",
      "[transformers] Both `max_new_tokens` (=10) and `max_length`(=20) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "You are a support ticket classifier.\n",
      "\n",
      "Ticket: mobile\n",
      "\n",
      "Return only one label (Billing, Technical, Account, General).\n",
      "\n"
     ]
    }
   ],
   "source": [
    "ticket = df[text_col].iloc[0]\n",
    "\n",
    "prompt = create_prompt(ticket)\n",
    "\n",
    "result = generator(prompt, max_new_tokens=10, do_sample=False)\n",
    "\n",
    "print(result[0][\"generated_text\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c0993d01-b711-4df2-9ee6-e47fc23ce06c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"full_text\"] = df[text_col].astype(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "41474445-2aab-4946-a88b-96d3f3423984",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"full_text\"] = df[text_col].fillna(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "87593324-07e7-4049-9650-530a405c27d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "ticket = df[\"full_text\"].iloc[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65723f54-b95e-4c9b-adfb-c907e3145d0a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
