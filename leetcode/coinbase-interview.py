text ='''eth 2000 2
btc 60000 3
eth 1900 29
btc 70000 4'''


class Solution:
    def calPrice(self,text) -> dict:
        textLine = text.split("\n")
        coin_to_num = {}
        for i in range(0,len(textLine)):
            linecxt = textLine[i].split(" ")
            coin = linecxt[0]
            num = float(linecxt[2])
            if coin in coin_to_num:
                coin_to_num[coin] += num
            else:
                coin_to_num[coin] = num
        coin_to_res = {}
        for i in range(0,len(textLine)):
            linecxt = textLine[i].split(" ")
            coin = linecxt[0]
            price = float(linecxt[1])
            num = float(linecxt[2])
            if coin in coin_to_res:
                coin_to_res[coin] += price * num / coin_to_num[coin]
            else:
                coin_to_res[coin] = price * num / coin_to_num[coin]
        return coin_to_res
    def printres(self,res: dict):
        for k,v in res.items():
            print("coin is ",k," price is ",v)

sol = Solution()
resdict = sol.calPrice(text)
sol.printres(resdict)