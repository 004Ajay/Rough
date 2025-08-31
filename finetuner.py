<<<<<<< HEAD
import torch
from datasets import load_dataset
from unsloth import FastLanguageModel, to_sharegpt, standardize_sharegpt
from trl import SFTTrainer
from transformers import TrainingArguments

# Step 1: Load a quantized, memory-efficient LLaMA 3 model using Unsloth
# This model has 8 billion parameters but uses 4-bit weights (saves memory!)
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",  # 8B LLaMA 3 model
    max_seq_length = 2048,   # Model can read up to 2048 tokens at a time
    dtype = None,            # Use default dtype
    load_in_4bit = True      # Load in 4-bit precision (very efficient)
)

# Step 2: Apply LoRA to specific attention layers
# LoRA enables efficient fine-tuning by injecting low-rank matrices into:
# q_proj: builds queries (what to look for)
# k_proj: builds keys (what exists)
# v_proj: builds values (content of keys)
# o_proj: projects output of attention layer

model = FastLanguageModel.get_peft_model(
    model,
    r = 4,  # Rank of LoRA adapter: smaller rank = fewer trainable params
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],  # Only apply LoRA to these layers
    use_gradient_checkpointing = "unsloth",  # Save memory during backpropagation
    lora_alpha = 16,  # Scaling factor for adapter output
    lora_dropout = 0,  # No dropout during training (can enable for regularization)
    bias = "none",  # Don't train bias terms (common in LoRA)
    use_rslora = False,  # Don’t use Rank-Scaling LoRA
    loftq_config = None  # (optional) for quantization-aware LoRA
)

# Step 3: Load a dataset — here, Alpaca-GPT4
dataset = load_dataset("vicgalle/alpaca-gpt4", split="train")

# Step 4: Convert dataset to ShareGPT-style chat format
dataset = to_sharegpt(
    dataset,
    merged_prompt = "{instruction}[[\nYour input is:\nf{input}]]",  # Custom instruction-input format
    output_column_name = "output",  # Where the response/answer lives
    conversation_extension = 3  # Extend short examples into conversations
)

# Step 5: Standardize formatting for training (tokens, EOS, etc.)
dataset = standardize_sharegpt(dataset)

# Step 6: Setup the trainer with training arguments
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = TrainingArguments(
        per_device_train_batch_size = 2,         # Small batch (since 8B model)
        gradient_accumulation_steps = 4,         # Acts like total batch size = 2×4 = 8
        max_steps = 60,                          # Train for 60 update steps
        learning_rate = 2e-4,                    # Slightly higher LR (LoRA-specific)
        optim = "adamw_8bit",                    # Memory-efficient optimizer
        weight_decay = 0.01,                     # Regularization to prevent overfitting
        output_dir = "/home/appuser/Desktop/Ajay/FineTuner/output"  # Where to save model
    )
)

# Step 7: Train the model
trainer_stats = trainer.train()

# Step 8: Save the final model with LoRA merged into base weights
# save_method = 'merged_16bit' saves the combined model (not just adapters)
model.save_pretrained_merged("model", tokenizer, save_method='merged_16bit')
=======
import torch
from datasets import load_dataset
from unsloth import FastLanguageModel, to_sharegpt, standardize_sharegpt
from trl import SFTTrainer
from transformers import TrainingArguments

# Step 1: Load a quantized, memory-efficient LLaMA 3 model using Unsloth
# This model has 8 billion parameters but uses 4-bit weights (saves memory!)
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",  # 8B LLaMA 3 model
    max_seq_length = 2048,   # Model can read up to 2048 tokens at a time
    dtype = None,            # Use default dtype
    load_in_4bit = True      # Load in 4-bit precision (very efficient)
)

# Step 2: Apply LoRA to specific attention layers
# LoRA enables efficient fine-tuning by injecting low-rank matrices into:
# q_proj: builds queries (what to look for)
# k_proj: builds keys (what exists)
# v_proj: builds values (content of keys)
# o_proj: projects output of attention layer

model = FastLanguageModel.get_peft_model(
    model,
    r = 4,  # Rank of LoRA adapter: smaller rank = fewer trainable params
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],  # Only apply LoRA to these layers
    use_gradient_checkpointing = "unsloth",  # Save memory during backpropagation
    lora_alpha = 16,  # Scaling factor for adapter output
    lora_dropout = 0,  # No dropout during training (can enable for regularization)
    bias = "none",  # Don't train bias terms (common in LoRA)
    use_rslora = False,  # Don’t use Rank-Scaling LoRA
    loftq_config = None  # (optional) for quantization-aware LoRA
)

# Step 3: Load a dataset — here, Alpaca-GPT4
dataset = load_dataset("vicgalle/alpaca-gpt4", split="train")

# Step 4: Convert dataset to ShareGPT-style chat format
dataset = to_sharegpt(
    dataset,
    merged_prompt = "{instruction}[[\nYour input is:\nf{input}]]",  # Custom instruction-input format
    output_column_name = "output",  # Where the response/answer lives
    conversation_extension = 3  # Extend short examples into conversations
)

# Step 5: Standardize formatting for training (tokens, EOS, etc.)
dataset = standardize_sharegpt(dataset)

# Step 6: Setup the trainer with training arguments
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = TrainingArguments(
        per_device_train_batch_size = 2,         # Small batch (since 8B model)
        gradient_accumulation_steps = 4,         # Acts like total batch size = 2×4 = 8
        max_steps = 60,                          # Train for 60 update steps
        learning_rate = 2e-4,                    # Slightly higher LR (LoRA-specific)
        optim = "adamw_8bit",                    # Memory-efficient optimizer
        weight_decay = 0.01,                     # Regularization to prevent overfitting
        output_dir = "/home/appuser/Desktop/Ajay/FineTuner/output"  # Where to save model
    )
)

# Step 7: Train the model
trainer_stats = trainer.train()

# Step 8: Save the final model with LoRA merged into base weights
# save_method = 'merged_16bit' saves the combined model (not just adapters)
model.save_pretrained_merged("model", tokenizer, save_method='merged_16bit')
>>>>>>> 4b72e3753e959bdf70550961b5bdadb09abb08d2
