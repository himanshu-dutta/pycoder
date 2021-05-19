from pycoder.imports import TrainingArguments, Trainer


def get_trainer(
    model: "torch.nn.Module",
    tokenizer: "transformer.PreTrainedTokenizer",
    train_ds: "torch.utils.data.Dataset",
    val_ds: "torch.utils.data.Dataset",
    cfg,
) -> "transformer.Trainer":
    training_args = TrainingArguments(
        output_dir=cfg.CHECKPOINT_PATH,
        num_train_epochs=cfg.EPOCHS,
        per_device_train_batch_size=cfg.TRAIN_BATCHSIZE,
        per_device_eval_batch_size=cfg.TRAIN_BATCHSIZE,
        gradient_accumulation_steps=cfg.BATCH_UPDATE,
        evaluation_strategy="epoch",
        fp16=cfg.FP16,
        fp16_opt_level=cfg.APEX_OPT_LEVEL,
        warmup_steps=cfg.WARMUP_STEPS,
        learning_rate=cfg.LR,
        adam_epsilon=cfg.EPS,
        weight_decay=0.01,
        save_total_limit=1,
        load_best_model_at_end=True,
        run_name=cfg.RUN_NAME,
        report_to="wandb",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        tokenizer=tokenizer,
    )

    return trainer
