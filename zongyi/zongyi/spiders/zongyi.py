import time
from copy import copy

import xlrd
import xlutils.copy
import xlwt
import scrapy



class ZongYiSpider(scrapy.Spider):
    name="zongyi"
    # allowed_domains = ["http://www.friok.com/tag/yxgengx"]
    # start_urls = ["http://www.friok.com/tag/yxgengx/page/1"]


    def start_requests(self):
        # url = "http://www.friok.com/category/gaoq/page/2"
        # headers = {
        #     "refer": "http://www.friok.com/category/gaoq/page/2",
        #     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        # }
        #
        # yield scrapy.Request(
        #     url=url,
        #     method="GET",
        #     headers=headers,
        #     callback=self.parse
        # )
        for i in range(3, 21):
            url = "http://www.friok.com/category/zongyi/page/" + str(i)
            headers = {
                "refer": "http://www.friok.com/category/zongyi/page/"+str(i),
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            }

            # global second_current
            # second_current = url
            # time.sleep(2)
            time.sleep(0.5)
            yield scrapy.Request(
                url=url,
                method="GET",
                headers=headers,
                callback=self.parse
            )

    def parse(self, response):
        print('11111111',type(response.request.headers),response.request.headers)
        print('11111111', response.headers)
        print('11111111', response.request.headers[b'Refer'])
        # print('11111111', type(response.request.headers.Refer))
        # print('11111111', response.headers)
        print('11111111', response.request)
        second_url_list = response.xpath("///html/body/div[@class='page']/div[@class='content']/div[@class='grid-m0s5 clearfix']/div[@class='col-main']/div/ul/li/div[@class='entry']/h2/a/@href").extract()
        print('second_url_list', second_url_list)
        for second_url in second_url_list:
            # print('second_url', second_url)
            headers = {
                "refer": response.request.headers[b'Refer'],
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            }
            time.sleep(0.5)
            yield scrapy.Request(
                url=second_url,
                meta={'second_url': second_url},
                headers=headers,
                dont_filter=True,
                method="GET",
                callback=self.second_parse
            )


    def second_parse(self, response):
        print('22222',response.meta['second_url'])
        # print('888888')
        # print(response.text)
        # third_url = response.xpath("///html/body/div[@class='page']/div[@class='content']/div[@class='grid-m0s5 clearfix']/div[@class='col-main']/div[@class='main-wrap']/div[@class='article clearfix']/div[@class='text']/div[@class='xydown_down_link']/p[4]/strong/a/@href").extract()
        # print('third_url', third_url)
        thrid_url = response.xpath("///html/body/div[@class='page']/div[@class='content']/div[@class='grid-m0s5 clearfix']/div[@class='col-main']/div[@class='main-wrap']/div[@class='article clearfix']/div[@class='text']/div[@class='xydown_down_link']/p[@class='downlink']/strong/a/@href").extract()
        # print('third_url', thrid_url)
        # global third_current
        headers = {
            "refer": response.meta['second_url'],
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        if len(thrid_url)==1:
            time.sleep(0.5)
            yield scrapy.Request(
                url=thrid_url[0],
                headers=headers,
                dont_filter=True,
                method="GET",
                callback=self.third_parse
            )

    def third_parse(self, response):
        plist = response.xpath("/html/body/div[@class='desc']/p")
        data = []
        for i in plist:
            data.append(i.xpath('string(.)').extract()[0])
        addr = response.xpath("/html/body/div[@class='list']/a/@href").extract()
        if len(addr)!=0:
            data.append(addr[0])
        print('00000',data)
        time.sleep(2)
        write(data)
        # print('999999',name)
        # mima = response.xpath("/html/body/div[@class='desc']/p[2]/text()")
        # / html / body / div[8] / a
        # / html / body / div[8] / a
        addr = response.xpath("/html/body/div[8]/@class").get()
        # for j in addr:
        # print("addr", addr)
        # print("addr", addr)
        # addr = response.xpath("/html/body/div[@class='list']/a/@href").extract()
        # print("name",name)
        # print("mima", mima)
        # print("addr", addr)



filename = "/Users/zhengruijie/Desktop/zongyi.xlsx"
def readline():
    wb = xlrd.open_workbook(filename)  #打开excel，保留文件格式
    sheet1 = wb.sheet_by_index(0)  #获取第一张表
    nrows = sheet1.nrows  #获取总行数
    ncols = sheet1.ncols
    return nrows
def write(info):
    data = xlrd.open_workbook(filename)
    ws = xlutils.copy.copy(data) #复制之前表里存在的数据
    table=ws.get_sheet(0)
    nownrows = readline()
    for i in range(len(info)):
        table.write(nownrows, i, label=info[i])  #最后一行追加数据
    # table.write(nownrows, 1, label=mima)
    # table.write(nownrows, 2, label=p)
    # table.write(nownrows, 3, label=url)
    ws.save(filename)  #保存的有旧数据和新数据
# write()


# if __name__ == '__main__':
#     write(d)
    # write_xlrd('1111')
    # scrapy
    # crawl
    # dianying
