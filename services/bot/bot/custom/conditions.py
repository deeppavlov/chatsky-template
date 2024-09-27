from chatsky import Context, BaseCondition


class IsUpperCase(BaseCondition):
    async def call(self, ctx: Context) -> bool:
        return ctx.last_request.text.isupper()
