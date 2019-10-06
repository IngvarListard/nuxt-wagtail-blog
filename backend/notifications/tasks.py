from backend.core.celery import app


@app.task
def test_task(test, test2):
    import logging
    logging.critical('TEST')
    print(test, test2)
    return test + test


@app.task
def periodic_test_task(a, b):
    print('Периодический таск с аргументами: ', a, b)
    return a + b


@app.task(name='core.tasks.task_with_custom_name', )
def task_with_some_props_1(a, b):
    print('Task with props 1')


@app.task(name='fail_task', max_retries=3, autoretry_for=(ValueError,), default_retry_delay=3)
def task_with_some_props_2(a, b):
    print('Task with retry, arguments: ', a, b)
    raise ValueError('this task will retry 3 times')


@app.task(name='task_with_uncaught_exception', max_retries=3, autoretry_for=(Exception,), throw=(ValueError,), default_retry_delay=3)
def task_with_some_props_3(a, b):
    print('Task with uncaught exception, params: ', a, b)
    raise ValueError('test value error that shouldn\'t be caught')


@app.task(name='task_with_delay_between_retry', autoretry_for=(Exception,), max_retries=3, default_retry_delay=3)
def task_with_some_props_4(a, b):
    print('Task with props 4')


@app.task(name='task_with_rate_limit', rate_limit='1/s', default_retry_delay=3)
def task_with_some_props_5(a, b):
    # rate_limit работает только в скоупе одного воркера
    print('limited task')
    import time
    time.sleep(10)


@app.task(name='task_with_time_limit', time_limit=5, default_retry_delay=3)
def task_with_some_props_6(a, b):
    print('task with time limit')
    import time
    time.sleep(7)
    print('Эта строка не должна быть достигнута')


@app.task(name='task_without_result', ignore_result=True, default_retry_delay=3)
def task_with_some_props_7(a, b):
    print('task without result')
    return 'no result'


@app.task(name='task_with_track_start', track_started=True, default_retry_delay=3)
def task_with_some_props_8(a, b):
    import time
    time.sleep(10)
