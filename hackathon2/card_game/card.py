class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    
    def __init__(self, rank, suit):
        self._rank=rank
        self._suit =suit

    def fromString(self,str):
        rank = str[0]
        suit = str[1]
        if rank == 'A':
            self._rank = 10
        else: 
            self._rank = int(rank)

        if suit == '♠':
            self._suit = 0
        elif suit == '♣':
            self._suit = 1
        elif suit == '♥':
            self._suit = 2
        elif suit == '♦':
            self._suit = 3
        pass

    def get_rank(self):
        return self._rank
      
    def set_rank(self, x):
        self._rank = x

    def get_suit(self):
        return self._suit
      
    def set_suit(self, x):
        self._suit = x

    def __str__(self):
        '''Hiển thị lá bài'''
        r = self._rank
        if(self._rank  == 10):
            r = 'A'
        s = self._suit
        if (s == 0) :
            s = '♠'
        if (s == 1) :
            s = '♣'
        if (s == 2) :
            s = '♥'
        if (s == 3) :
            s = '♦'
        return f'{r}{s}'
    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        if  not isinstance(other,Card):
            return False

        if self._suit == other._suit:
            return self._rank > other._rank
        return self._suit > other._suit

#L1 = Card(7,3)
#L2 = Card(6,1)
#L3 = Card(8,0)
#L4 = Card(10,2)
#print(L1>L2)
#print(L1)
#print(L2)
#print(L3)
#print(L4)
