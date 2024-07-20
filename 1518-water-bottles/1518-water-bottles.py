class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
            drink=numBottles#15
            ex=0
            while numBottles>=numExchange:
                dr=numBottles//numExchange #3
                ex=numBottles%numExchange
                numBottles=dr+ex #6
                drink+=dr #3
            return drink



        