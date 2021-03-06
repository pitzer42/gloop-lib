import asyncio


def make_async_mock(mock, result=None):
    future = asyncio.Future()
    future.set_result(result)
    mock.return_value = future
