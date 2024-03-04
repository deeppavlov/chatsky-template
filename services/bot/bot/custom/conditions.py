from dff.script import Context


def is_upper_case(ctx: Context, pipeline):
    return ctx.last_request.text.isupper()
