def _10_softmax():
    """10. Softmax."""
    import numpy as np

    # SCORES = [3.0, 1.0, 0.2]
    # SCORES = np.array([[1, 2, 3, 6],
    #                    [2, 4, 5, 6],
    #                    [3, 8, 7, 6]])
    # SCORES = np.array([2.0, 6.0, 0.1, 9.0, 1.0])
    SCORES = np.array([3.0, 1.0, 0.2])

    def softmax(x):
        """Compute softmax values for each sets of SCORES in x."""
        # pass  # TODO: Compute and return softmax(x)
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    print("softmax(score) : \n",softmax(SCORES/10))
    # print("softmax(score) : \n",softmax(SCORES*10))


    def display_graph():
        """ show the probablity layed between 0.0 ~ 1.0
          The graph shows how probablity changed
        """
        # Plot softmax curves
        import matplotlib.pyplot as plt
        x = np.arange(-2.0, 6.0, 0.1)
        SCORES = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

        plt.plot(x, softmax(SCORES).T, linewidth=2)
        plt.show()
    display_graph()
# _10_softmax()
