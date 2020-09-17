luk, donnachie, mcandrew

import seaborn as sns
import matplotlib.pyplot as plt

#from McAndrew's model_v0.2 notes
# ----- code for plotting ---------------------------------------------------------------------------
    # let's move this code to a separate python script called visualCheck.py insidet our same folder

    sns.style.use("fivethirtyright")

    fig,ax = plt.subplots()

    d = singleEWForecast
    ax.plot( d.numnewcases_mid, d.prob, "b-", linewidth=2 )
    
    ax.set_xlabel("Number of new cases", fontsize=10)
    ax.set_xlabel("PMF", fontsize=10)

    ax.tick_params(size=2.,direction="in")

    ax.text(0.99,0.99,"Equally Weighted Ensemble"
            ,ha='right',va='top',transform=ax.transAxes)

    plt.savefig("visualCheckProbDist.pdf")
    plt.close()