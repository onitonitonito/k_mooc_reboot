import numpy as np
import matplotlib.pyplot as plt

def plotSinWave(**kwargs) : # this is test for single curve.
	""" plot sine wave using **Kwargs (keyworded args) factors
    arg = kwargs.get('arg',number) : default arg = number
    """
	endTime = kwargs.get('endTime', 1)
	sampleTime = kwargs.get('sampleTime', 0.01)
	amp = kwargs.get('amp', 1)
	freq = kwargs.get('freq', 1)
	startTime = kwargs.get('startTime', 0)
	bias = kwargs.get('bias', 0)

	time = np.arange(0.0, endTime, sampleTime)
	result = amp * np.sin(2*np.pi*freq*time + startTime) + bias

	plt.plot(time, result)
	plt.grid(True)
	plt.xlabel('time')
	plt.ylabel('sin')
	plt.show()


class sinWaveForm:
    def __init__(self, **kwargs) :
        self.endTime = kwargs.get('endTime', 1)
        self.sampleTime = kwargs.get('sampleTime', 0.01)
        self.amp = kwargs.get('amp', 1)
        self.freq = kwargs.get('freq', 1)
        self.startTime = kwargs.get('startTime', 0)
        self.bias = kwargs.get('bias', 0)

    def calcDomain(self) :
        return np.arange(0.0, self.endTime, self.sampleTime)

    def calcSinValue(self, time) :
        return self.amp * np.sin(2*np.pi*self.freq*time + self.startTime) + self.bias

    def plotWave(self) :
        time = self.calcDomain()
        result = self.calcSinValue(time)

        plt.plot(time, result)
        plt.grid(True)
        plt.xlabel('time')
        plt.ylabel('sin')
        plt.show()


if __name__ == "__main__" :
    # test = sinWaveForm(amp = 1, endTime = 1)
    # test1.plotWave()

    # plotSinWave(amp = 2, endTime = 3)   # close every screen
    # plotSinWave(freq = 5, endTime = 3)
    # plotSinWave(freq = 7, endTime = 3)

    test2 = sinWaveForm(amp = 2, freq=0.25, endTime = 5)
    test3 = sinWaveForm(amp = 0.5, freq=4, endTime = 5)

    time = test2.calcDomain()
    resultTest2 = test2.calcSinValue(time)
    resultTest3 = test3.calcSinValue(time)

    plt.plot(time, resultTest2,
            time, resultTest3,
            time, resultTest2+resultTest3)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel('Two sin curves combine')
    plt.show()

    # test.endTime = 2
    # print(test.calcDomain())
    # print(test.calcSinValue(test.calcDomain()))
    # test.plotWave()

# refer: http://pinkwink.kr/707 [PinkWink]
