__author__ = 'MoroJoJo'
# coding = utf-8


from stl_utils import stl_logger as slog

import tushare
import pandas as pd
import os


'''
获取投资参考数据
'''


PROFIT_INFO_COUNT = 200       # 获取的分配预案数据条数
DATA_YEAR = 2016              # 获取数据的年份
DATA_QUARTER = 1              # 获取数据的季度
DATA_MONTH = 1                # 获取数据的月份

RETRY_COUNT = 5               # 调用tushare接口失败重试次数
RETRY_PAUSE = 0.1             # 调用tushare接口失败重试间隔时间

DEFAULT_DIR_PATH = '../../../Data/origin/tushare/security_reference_data'


def get_profit_data(year, top):
    '''
    获取指定年份的股票的分配预案

        code:股票代码
        name:股票名称
        year:分配年份
        report_date:公布日期
        divi:分红金额（每10股）
        shares:转增和送股数（每10股）

    Parameters
    ------
        year: 预案公布的年份
        top: 取最新数据的条数
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/profit(%d:1-%d).csv' % (dir_path, year, top)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.profit_data: year=%s, count=%d' % (year, PROFIT_INFO_COUNT))
        tmp_data = tushare.profit_data(year=year, top=top, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.profit_data(%s) excpetion, args: %s' % (year, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.profit_data(%s) return none' % year)
    else:
        tmp_data.to_csv(file_path)


def get_forcast_data(year, quarter):
    '''
    获取指定年份季度的股票的业绩预告

        code,代码
        name,名称
        type,业绩变动类型【预增、预亏等】
        report_date,发布日期
        pre_eps,上年同期每股收益
        range,业绩变动范围

    Parameters
    ------
        year: 年度
        quarter: 季度
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/forecast(%dQ%d).csv' % (dir_path, year, quarter)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.forecast_data: year=%d, quarter=%d' % (year, quarter))
        tmp_data = tushare.forecast_data(year=year, quarter=quarter)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.forecast_data(%d, %d) excpetion, args: %s' % (year, quarter, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.forecast_data(%d, %d) return none' % (year, quarter))
    else:
        tmp_data.to_csv(file_path)


def get_restricted_stock_data(year, month):
    '''
    获取指定年份月份的股票限售股解禁数据

        code：股票代码
        name：股票名称
        date:解禁日期
        count:解禁数量（万股）
        ratio:占总盘比率

    Parameters
    ------
        year: 年度
        month: 月份
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/restricted_share(%d-%d).csv' % (dir_path, year, month)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.xsg_data: year=%d, month=%d' % (year, month))
        tmp_data = tushare.xsg_data(year=year, month=month, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.xsg_data(%d, %d) excpetion, args: %s' % (year, month, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.xsg_data(%d, %d) return none' % (year, month))
    else:
        tmp_data.to_csv(file_path)


def get_fund_holding_data(year, quarter):
    '''
    获取指定年份季度的基金持有股票数据

        code：股票代码
        name：股票名称
        date:报告日期
        nums:基金家数
        nlast:与上期相比（增加或减少了）
        count:基金持股数（万股）
        clast:与上期相比
        amount:基金持股市值
        ratio:占流通盘比率

    Parameters
    ------
        year: 年度
        quarter: 季度
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/fund_holding(%dQ%d).csv' % (dir_path, year, quarter)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.fund_holdings: year=%d, quarter=%d' % (year, quarter))
        tmp_data = tushare.fund_holdings(year=year, quarter=quarter, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.fund_holdings(%d, %d) excpetion, args: %s' % (year, quarter, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.fund_holdings(%d, %d) return none' % (year, quarter))
    else:
        tmp_data.to_csv(file_path)


def get_new_security_data():
    '''
    获取新股数据

        code：股票代码
        name：股票名称
        ipo_date:上网发行日期
        issue_date:上市日期
        amount:发行数量(万股)
        markets:上网发行数量(万股)
        price:发行价格(元)
        pe:发行市盈率
        limit:个人申购上限(万股)
        funds：募集资金(亿元)
        ballot:网上中签率(%)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/new_security.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.new_stocks')
        tmp_data = tushare.new_stocks(retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.new_stocks excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.new_stocks return none')
    else:
        tmp_data.to_csv(file_path)


def get_margin_trade_data_sh(start_date, end_date):
    '''
    获取上证交易所股票的融资融券数据

        opDate:信用交易日期
        rzye:本日融资余额(元)
        rzmre: 本日融资买入额(元)
        rqyl: 本日融券余量
        rqylje: 本日融券余量金额(元)
        rqmcl: 本日融券卖出量
        rzrqjyzl:本日融资融券余额(元)

    Parameters
    ------
        start_date:统计开始日期
        end_date:统计结束日期
    return
    -------
        无
    '''
    dir_path = '%s/margin_trade/summary/' % DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/sh_margins(%s--%s).csv' % (dir_path, start_date, end_date)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.sh_margins, start=%s, end=%s' % (start_date, end_date))
        tmp_data = tushare.sh_margins(start=start_date, end=end_date, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.sh_margins, start=%s, end=%s, excpetion, args: %s' % (start_date, end_date, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.sh_margins, start=%s, end=%s return none' % (start_date, end_date))
    else:
        tmp_data.to_csv(file_path)


def get_margin_trade_detail_data_sh(start_date, end_date, code):
    '''
    获取上证交易所股票的融资融券详细数据

        opDate:信用交易日期
        stockCode:标的证券代码
        securityAbbr:标的证券简称
        rzye:本日融资余额(元)
        rzmre: 本日融资买入额(元)
        rzche:本日融资偿还额(元)
        rqyl: 本日融券余量
        rqmcl: 本日融券卖出量
        rqchl: 本日融券偿还量

    Parameters
    ------
        start_date:统计开始日期
        end_date:统计结束日期
        code:股票代码
    return
    -------
        无
    '''
    dir_path = '%s/margin_trade/detail/sh' % DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/%s(%s--%s).csv' % (dir_path, code, start_date, end_date)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.sh_margin_details, code=%s, start=%s, end=%s' % (code, start_date, end_date))
        tmp_data = tushare.sh_margin_details(start=start_date, end=end_date, symbol=code, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.sh_margin_details, cod=%s, start=%s, end=%s, excpetion, args: %s' % (code, start_date, end_date, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.sh_margin_details, code=%s, start=%s, end=%s return none' % (code, start_date, end_date))
    else:
        tmp_data.to_csv(file_path)


def get_margin_trade_data_sz(start_date, end_date):
    '''
    获取深圳交易所股票的融资融券数据

        opDate:信用交易日期
        rzye:本日融资余额(元)
        rzmre: 本日融资买入额(元)
        rqyl: 本日融券余量
        rqylje: 本日融券余量金额(元)
        rqmcl: 本日融券卖出量
        rzrqjyzl:本日融资融券余额(元)

    Parameters
    ------
        start_date:统计开始日期
        end_date:统计结束日期
    return
    -------
        无
    '''
    dir_path = '%s/margin_trade/summary/' % DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/sz_margins(%s--%s).csv' % (dir_path, start_date, end_date)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.sz_margins, start=%s, end=%s' % (start_date, end_date))
        tmp_data = tushare.sz_margins(start=start_date, end=end_date, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.sz_margins, start=%s, end=%s, excpetion, args: %s' % (start_date, end_date, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.sz_margins, start=%s, end=%s return none' % (start_date, end_date))
    else:
        tmp_data.to_csv(file_path)


def get_margin_trade_detail_data_sz(start_date, end_date, code):
    '''
    获取深圳交易所股票的融资融券详细数据

        opDate:信用交易日期
        stockCode:标的证券代码
        securityAbbr:标的证券简称
        rzye:本日融资余额(元)
        rzmre: 本日融资买入额(元)
        rzche:本日融资偿还额(元)
        rqyl: 本日融券余量
        rqmcl: 本日融券卖出量
        rqchl: 本日融券偿还量

    Parameters
    ------
        start_date:统计开始日期
        end_date:统计结束日期
        code:股票代码
    return
    -------
        无
    '''
    dir_path = '%s/margin_trade/detail/sz' % DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/%s(%s--%s).csv' % (dir_path, code, start_date, end_date)

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.sh_margin_details, code=%s, start=%s, end=%s' % (code, start_date, end_date))
        tmp_data = tushare.sh_margin_details(start=start_date, end=end_date, symbol=code, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
    except Exception as exception:
        slog.StlDmLogger().error('tushare.sh_margin_details, cod=%s, start=%s, end=%s, excpetion, args: %s' % (code, start_date, end_date, exception.args.__str__()))

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.sh_margin_details, code=%s, start=%s, end=%s return none' % (code, start_date, end_date))
    else:
        tmp_data.to_csv(file_path)


if __name__ == '__main__':
    get_profit_data(DATA_YEAR, PROFIT_INFO_COUNT)
    get_forcast_data(DATA_YEAR, DATA_QUARTER)
    get_restricted_stock_data(DATA_YEAR, DATA_MONTH)
    get_fund_holding_data(DATA_YEAR, DATA_QUARTER)
    get_new_security_data()
    get_margin_trade_data_sh(start_date='2016-07-01', end_date='2016-08-02')
    get_margin_trade_detail_data_sh(start_date='2016-07-01', end_date='2016-08-02', code='600789')
    get_margin_trade_data_sz(start_date='2016-07-01', end_date='2016-08-02')
    get_margin_trade_detail_data_sz(start_date='2016-07-01', end_date='2016-08-02', code='000002')