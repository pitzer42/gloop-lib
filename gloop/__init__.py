from gloop.channels import Channel


class BreakTransformLoop(Exception):
    pass


async def transform_step(
        f,
        channel_in: Channel,
        channel_out: Channel):

    x = await channel_in.receive()
    y = await f(x)
    if y is not None:
        await channel_out.send(y)
    return y


async def transform_loop(
        func,
        channel_in: Channel,
        channel_out: Channel):

    try:
        while True:
            await transform_step(
                func,
                channel_in,
                channel_out
            )
    except BreakTransformLoop:
        pass
