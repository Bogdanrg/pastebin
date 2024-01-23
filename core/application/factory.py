import asyncio
from functools import partial
from typing import Callable, Coroutine, Iterable

from fastapi import APIRouter, FastAPI


def create(
        *_,
        rest_routers: Iterable[APIRouter],
        startup_tasks: Iterable[Callable[[], Coroutine]] | None = None,
        shutdown_tasks: Iterable[Callable[[], Coroutine]] | None = None,
        **kwargs,
) -> FastAPI:
    app = FastAPI(**kwargs)

    for router in rest_routers:
        app.include_router(router)

    if startup_tasks:
        for task in startup_tasks:
            coro = partial(asyncio.create_task, task())
            app.on_event("startup")(coro)

    if shutdown_tasks:
        for task in shutdown_tasks:
            app.on_event("shutdown")(task)

    return app
