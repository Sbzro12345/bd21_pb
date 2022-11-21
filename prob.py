#change arr to suit the needs
#arr takes probabilities as percentages, and returns them in form /256
#used to calculate required probabilities of BDv21 spawning RNG
arr = [25,25,25,25]

def prob(n):
    if n == 1:
        return [ (arr[0]/100*256) ]
    else:
        x = 1
        for i in range (0,n-1):
            x = x * (1- (prob(n-1)[i])/256 )
            
        y = prob(n-1)+[ (arr[n-1]/100*256) / x]
        return y

print(prob(len(arr)))
input()
