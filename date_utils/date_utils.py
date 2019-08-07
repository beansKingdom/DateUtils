import datetime
import time


def compute_interval_days(interval_days, input_time=None):
    """
    @:param: interval_days(int), input_time(datetime.datetime.now())
    计算指定时间在间隔天数后的时间, 如果未传入指定时间则以当前时间为准。
    @:return "yyyy-mm-dd"
    example:
        now-time: 2019-08-06
        compute_interval_days(-3) ==> 2019-08-03
        compute_interval_days(3) ==> 2019-08-09
    """

    if not input_time:
        input_time = datetime.date.today()
    else:
        if isinstance(input_time, datetime.date):
            pass
        else:
            raise Exception("传入时间类型错误, 应该为 datetime.date()")

    output_time = input_time + datetime.timedelta(days=int(interval_days))
    return output_time


def compute_time_stamp():
    """
    返回当前时间的毫秒时间戳
    """
    now_time = time.time()
    now_time_stamp = int(round(now_time * 1000))
    return now_time_stamp


"""
返回当前时间之间某个时间段的毫秒时间戳
@:param: interval_time: 间隔时间（秒）
"""


def compute_time_delta(interval_time=0):
    now_time = datetime.datetime.now()
    past_time = now_time - datetime.timedelta(seconds=interval_time)
    t_time = time.mktime(past_time.timetuple()) + past_time.microsecond / 1E6
    return int(round(t_time * 1000))


def compute_time(interval=0):
    """
    返回当前时间的年月日格式: yyyy-mm-dd
    interval: 与当前时间的间隔日期
    example: interval = 1表示一天后的时间, -1表示前一天的时间
    """

    if not isinstance(interval, int):
        raise ValueError("input value error, params must be int type")

    now_time = datetime.datetime.now()
    if interval >= 0:
        real_time = now_time + datetime.timedelta(days=interval)
    else:
        real_time = now_time - datetime.timedelta(days=-interval)
    day_format = "%Y-%m-%d"
    day_str = real_time.strftime(day_format)
    return day_str


def compute_last_week_time():
    """
    根据当天的时间查询上周的开始时间和结束时间 (返回时间为上上周6到上周6的日期)
    返回格式: yyyy-mm-dd, yyyy-mm-dd
    :return start_time, end_time
    """
    now_time = datetime.datetime.now()
    day_format = "%Y-%m-%d"
    end_time = now_time - datetime.timedelta(days=(now_time.weekday() + 3))
    start_time = end_time - datetime.timedelta(days=6)
    start_time_str = start_time.strftime(day_format)
    end_time_str = end_time.strftime(day_format)
    return start_time_str, end_time_str


def compute_interval_day(input_time):
    """
    传入指定时间，计算与当前时间与传入时间之间的间隔天数
    :param input_time
    type: str, format: "%Y-%m-%d"
    """
    now_time = datetime.datetime.now()
    day_format = "%Y-%m-%d"

    end_time_str = now_time.strftime(day_format)
    start_time_str = input_time.strftime(day_format)

    end_sec = time.mktime(time.strptime(end_time_str, day_format))
    start_sec = time.mktime(time.strptime(start_time_str, day_format))

    work_days = int((end_sec - start_sec) / (24 * 60 * 60))
    return work_days


def compute_timestamp(time_str, time_format):
    """
    返回指定时间的时间戳, 返回时间戳(精度秒)
    """
    return int(time.mktime(datetime.datetime.strptime(time_str, time_format).timetuple()))


if __name__ == '__main__':
    print(compute_interval_days(-3))
    # a.compute_interval_days(-3)
    # print(DateComputeUtil.compute_time_stamp())
    # print(DateComputeUtil.compute_time_delta(60))
    # print(DateComputeUtil.compute_time_delta(0))
    # print(DateComputeUtil.compute_time())
    # print(DateUtils.compute_last_week_time())
    # print(DateComputeUtil.compute_interval_day(datetime.datetime(2019,7,1,10,30,30)))
    # print()
    pass
