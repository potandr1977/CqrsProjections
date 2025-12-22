class PersonHandler:
    async def handle(self, message: str):
        print(f"[HANDLER] Обрабатываю сообщение: {message}")
