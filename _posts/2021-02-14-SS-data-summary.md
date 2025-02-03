---
layout: post
title: Quick Soil Sampling Data Summary With Python
subtitle: Using pandas, matplotlib, and numpy to create a quick and dirty plot that summarized your data. Just enough to make your job easier.
tags: [python, geology, exploration, soil sampling, data, pandas, matplotlib, numpy]
---

Geologists often use soil sampling methods in mineral exploration to gather information about elements anomaly in the soil of a certain area. The output of this activity is a database containing coordinates and various elements concentration from the sample taken at that point. Before diving deep into the data and doing any fancy analysis, it is always a good idea to familiarize ourselves with the data by looking into the summary statistics and the general and spatial relationship of the data as a whole. By using python we can write a simple code to get the summary statistics and some useful graphs to summarize the data in just a few minutes.

We will use `pandas`, `numpy`, and `matplotib` libraries for this code, so let's begin with importing our library


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

We can use `pandas` to read our dataset and put it into a variable called *data*. We can then use `head()` function from `pandas` to look at the first 5 rows of the data.


```python
data = pd.read_csv('soil_data_example.csv')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EASTING</th>
      <th>NORTHING</th>
      <th>Mg</th>
      <th>Al</th>
      <th>Si</th>
      <th>P</th>
      <th>S</th>
      <th>Cl</th>
      <th>Ca</th>
      <th>Ti</th>
      <th>...</th>
      <th>Cd</th>
      <th>Sn</th>
      <th>Sb</th>
      <th>W</th>
      <th>Hg</th>
      <th>Pb</th>
      <th>Bi</th>
      <th>Th</th>
      <th>U</th>
      <th>LE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>803041</td>
      <td>9880671</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>53.495</td>
      <td>86.0</td>
      <td>686.0</td>
      <td>149</td>
      <td>405.0</td>
      <td>6.244</td>
      <td>...</td>
      <td>0</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>31.0</td>
      <td>0</td>
      <td>39</td>
      <td>0</td>
      <td>844.453</td>
    </tr>
    <tr>
      <th>1</th>
      <td>803137</td>
      <td>9880700</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>53.272</td>
      <td>84.0</td>
      <td>660.0</td>
      <td>0</td>
      <td>461.0</td>
      <td>5.452</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>66.0</td>
      <td>0</td>
      <td>41</td>
      <td>4</td>
      <td>813.117</td>
    </tr>
    <tr>
      <th>2</th>
      <td>803055</td>
      <td>9880624</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>57.548</td>
      <td>154.0</td>
      <td>621.0</td>
      <td>0</td>
      <td>203.0</td>
      <td>6.865</td>
      <td>...</td>
      <td>0</td>
      <td>95</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>41.0</td>
      <td>0</td>
      <td>37</td>
      <td>0</td>
      <td>831.336</td>
    </tr>
    <tr>
      <th>3</th>
      <td>803150</td>
      <td>9880652</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>68.581</td>
      <td>101.0</td>
      <td>684.0</td>
      <td>0</td>
      <td>325.0</td>
      <td>6.396</td>
      <td>...</td>
      <td>0</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>58.0</td>
      <td>0</td>
      <td>38</td>
      <td>0</td>
      <td>834.693</td>
    </tr>
    <tr>
      <th>4</th>
      <td>803070</td>
      <td>9880576</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>73.638</td>
      <td>184.0</td>
      <td>758.0</td>
      <td>0</td>
      <td>251.0</td>
      <td>7.636</td>
      <td>...</td>
      <td>26</td>
      <td>126</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>68.0</td>
      <td>0</td>
      <td>31</td>
      <td>0</td>
      <td>819.252</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 37 columns</p>
</div>



>*Note: for this example, we use data with dummy coordinates.*

## Summary statistics

By using `pandas`, getting summary statistics is as simple as this:


```python
pd.set_option('display.max_columns', None)
data.iloc[:,2:].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mg</th>
      <th>Al</th>
      <th>Si</th>
      <th>P</th>
      <th>S</th>
      <th>Cl</th>
      <th>Ca</th>
      <th>Ti</th>
      <th>V</th>
      <th>Cr</th>
      <th>Mn</th>
      <th>Fe</th>
      <th>Co</th>
      <th>Ni</th>
      <th>Cu</th>
      <th>Zn</th>
      <th>As</th>
      <th>Se</th>
      <th>Rb</th>
      <th>Sr</th>
      <th>Y</th>
      <th>Zr</th>
      <th>Nb</th>
      <th>Mo</th>
      <th>Ag</th>
      <th>Cd</th>
      <th>Sn</th>
      <th>Sb</th>
      <th>W</th>
      <th>Hg</th>
      <th>Pb</th>
      <th>Bi</th>
      <th>Th</th>
      <th>U</th>
      <th>LE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
      <td>483.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.361609</td>
      <td>37.306886</td>
      <td>79.901859</td>
      <td>164.188741</td>
      <td>635.832406</td>
      <td>108.314700</td>
      <td>447.012607</td>
      <td>4.826319</td>
      <td>35.511387</td>
      <td>67.778468</td>
      <td>75.228035</td>
      <td>65.516644</td>
      <td>256.832961</td>
      <td>14.291925</td>
      <td>22.339545</td>
      <td>50.455487</td>
      <td>43.819876</td>
      <td>1.204969</td>
      <td>90.469979</td>
      <td>19.761905</td>
      <td>30.440994</td>
      <td>322.449275</td>
      <td>25.619048</td>
      <td>1.917184</td>
      <td>90.842650</td>
      <td>5.383023</td>
      <td>14.844720</td>
      <td>5.236025</td>
      <td>0.409938</td>
      <td>0.300207</td>
      <td>49.049996</td>
      <td>0.267081</td>
      <td>31.828157</td>
      <td>0.389234</td>
      <td>799.849393</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.524420</td>
      <td>19.170464</td>
      <td>21.018874</td>
      <td>105.011094</td>
      <td>116.399578</td>
      <td>166.519336</td>
      <td>364.993895</td>
      <td>1.125096</td>
      <td>27.704977</td>
      <td>72.420758</td>
      <td>132.400090</td>
      <td>48.937698</td>
      <td>266.687782</td>
      <td>16.964439</td>
      <td>21.153868</td>
      <td>42.358326</td>
      <td>47.032683</td>
      <td>1.866225</td>
      <td>53.418809</td>
      <td>14.534807</td>
      <td>7.541458</td>
      <td>108.510507</td>
      <td>6.765470</td>
      <td>5.917603</td>
      <td>78.306505</td>
      <td>10.428192</td>
      <td>67.141786</td>
      <td>22.061828</td>
      <td>2.077758</td>
      <td>1.339993</td>
      <td>89.163245</td>
      <td>2.859267</td>
      <td>13.579391</td>
      <td>1.446719</td>
      <td>40.073827</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>38.589000</td>
      <td>0.000000</td>
      <td>1.004000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.137000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>4.597000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>11.000000</td>
      <td>7.000000</td>
      <td>13.000000</td>
      <td>104.000000</td>
      <td>9.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>631.444000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>40.015500</td>
      <td>63.242000</td>
      <td>96.500000</td>
      <td>565.500000</td>
      <td>0.000000</td>
      <td>1.376500</td>
      <td>3.935000</td>
      <td>19.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>24.906500</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>8.000000</td>
      <td>22.000000</td>
      <td>16.000000</td>
      <td>0.000000</td>
      <td>50.500000</td>
      <td>12.000000</td>
      <td>26.000000</td>
      <td>247.500000</td>
      <td>21.000000</td>
      <td>0.000000</td>
      <td>27.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>21.000000</td>
      <td>0.000000</td>
      <td>22.000000</td>
      <td>0.000000</td>
      <td>776.857500</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>44.624000</td>
      <td>77.059000</td>
      <td>154.000000</td>
      <td>637.000000</td>
      <td>0.000000</td>
      <td>536.000000</td>
      <td>4.613000</td>
      <td>37.000000</td>
      <td>42.000000</td>
      <td>32.000000</td>
      <td>47.867000</td>
      <td>159.000000</td>
      <td>12.000000</td>
      <td>18.000000</td>
      <td>37.000000</td>
      <td>31.000000</td>
      <td>0.000000</td>
      <td>76.000000</td>
      <td>16.000000</td>
      <td>30.000000</td>
      <td>313.000000</td>
      <td>25.000000</td>
      <td>0.000000</td>
      <td>65.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>30.000000</td>
      <td>0.000000</td>
      <td>811.330000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.000000</td>
      <td>48.510000</td>
      <td>95.729000</td>
      <td>251.000000</td>
      <td>702.000000</td>
      <td>191.500000</td>
      <td>774.000000</td>
      <td>5.567500</td>
      <td>50.000000</td>
      <td>108.000000</td>
      <td>75.500000</td>
      <td>101.228000</td>
      <td>483.000000</td>
      <td>22.000000</td>
      <td>30.000000</td>
      <td>68.000000</td>
      <td>54.000000</td>
      <td>2.000000</td>
      <td>118.000000</td>
      <td>22.000000</td>
      <td>34.000000</td>
      <td>385.500000</td>
      <td>29.000000</td>
      <td>0.000000</td>
      <td>147.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>39.000000</td>
      <td>0.000000</td>
      <td>42.000000</td>
      <td>0.000000</td>
      <td>829.934000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>22.825000</td>
      <td>77.831000</td>
      <td>150.081000</td>
      <td>465.000000</td>
      <td>970.000000</td>
      <td>830.000000</td>
      <td>999.000000</td>
      <td>9.502000</td>
      <td>337.000000</td>
      <td>385.000000</td>
      <td>896.000000</td>
      <td>243.907000</td>
      <td>989.000000</td>
      <td>232.000000</td>
      <td>145.000000</td>
      <td>490.000000</td>
      <td>455.000000</td>
      <td>12.000000</td>
      <td>309.000000</td>
      <td>149.000000</td>
      <td>59.000000</td>
      <td>735.000000</td>
      <td>45.000000</td>
      <td>96.000000</td>
      <td>351.000000</td>
      <td>55.000000</td>
      <td>827.000000</td>
      <td>223.000000</td>
      <td>22.000000</td>
      <td>12.000000</td>
      <td>867.000000</td>
      <td>45.000000</td>
      <td>66.000000</td>
      <td>13.000000</td>
      <td>865.822000</td>
    </tr>
  </tbody>
</table>
</div>



For practicality, `pandas` by default will not show the full range of rows and columns of our dataset. The first line of the code tells `pandas` to show the full range of the columns. In the second line, we use `iloc[:, 2:]` attribute to ignore the first two columns of our dataset because we don't need summary statistics of the x and y coordinate (unless for some reason you do).

## Histograms

Next, we will draw the histogram of each element's concentration in the area. Because of the logarithmic nature of element concentration in the soil, we will plot the log concentration value into the histogram. 
Since we are dealing with a lot of 0's, we will add a very small value to all the concentration data to make it easier with the logarithmic transformation. There are various ways to deal with zero values in the dataset, but for this example, let's just add `0.0001` to all concentration data.


```python
data.iloc[:,2:] = np.log(data.iloc[:,2:]+0.0001)
```

`np.log` is a natural logarithm with base *e* if we want logarithm transformation with base *10* we can use `np.log10`. Now if we call `data.head()` we will see that that the concentration of each element already transformed into its logarithmic value.

>*Note: code above will return an error if there are still zero values in the datasets. There are various ways to deals with `0` and `NaN` value in our dataset and it was up to you which method you will use for your case. You can also ignore this line if you don't want to do any logarithmic transformation for your dataset*


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EASTING</th>
      <th>NORTHING</th>
      <th>Mg</th>
      <th>Al</th>
      <th>Si</th>
      <th>P</th>
      <th>S</th>
      <th>Cl</th>
      <th>Ca</th>
      <th>Ti</th>
      <th>V</th>
      <th>Cr</th>
      <th>Mn</th>
      <th>Fe</th>
      <th>Co</th>
      <th>Ni</th>
      <th>Cu</th>
      <th>Zn</th>
      <th>As</th>
      <th>Se</th>
      <th>Rb</th>
      <th>Sr</th>
      <th>Y</th>
      <th>Zr</th>
      <th>Nb</th>
      <th>Mo</th>
      <th>Ag</th>
      <th>Cd</th>
      <th>Sn</th>
      <th>Sb</th>
      <th>W</th>
      <th>Hg</th>
      <th>Pb</th>
      <th>Bi</th>
      <th>Th</th>
      <th>U</th>
      <th>LE</th>
    </tr>
    <!-- Begin section for dataframe table formatting -->
    <style type="text/css">
    table.dataframe {
        width: 100%;
        height: 240px;
        display: block;
        overflow: auto;
        font-family: Arial, sans-serif;
        font-size: 13px;
        line-height: 20px;
        text-align: center;
    }
    table.dataframe th {
      font-weight: bold;
      padding: 4px;
    }
    table.dataframe td {
      padding: 4px;
    }
    table.dataframe tr:hover {
      background: #b8d1f3; 
    }
    </style>
    <!-- End section for dataframe table formatting -->
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>803041</td>
      <td>9880671</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>3.979590</td>
      <td>4.454348</td>
      <td>6.530878</td>
      <td>5.003947</td>
      <td>6.003887</td>
      <td>1.831637</td>
      <td>3.135499</td>
      <td>3.761202</td>
      <td>-9.210340</td>
      <td>3.880823</td>
      <td>4.543296</td>
      <td>2.302595</td>
      <td>2.302595</td>
      <td>4.219509</td>
      <td>4.060445</td>
      <td>-9.21034</td>
      <td>3.044527</td>
      <td>2.484915</td>
      <td>3.555351</td>
      <td>6.146329</td>
      <td>3.367299</td>
      <td>-9.21034</td>
      <td>3.713575</td>
      <td>-9.21034</td>
      <td>3.555351</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>3.433990</td>
      <td>-9.21034</td>
      <td>3.663564</td>
      <td>-9.210340</td>
      <td>6.738689</td>
    </tr>
    <tr>
      <th>1</th>
      <td>803137</td>
      <td>9880700</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>3.975413</td>
      <td>4.430818</td>
      <td>6.492240</td>
      <td>-9.210340</td>
      <td>6.133398</td>
      <td>1.696001</td>
      <td>3.295841</td>
      <td>4.812185</td>
      <td>6.284134</td>
      <td>4.346828</td>
      <td>5.752573</td>
      <td>2.772595</td>
      <td>-9.210340</td>
      <td>4.700481</td>
      <td>4.709531</td>
      <td>-9.21034</td>
      <td>3.761202</td>
      <td>2.833219</td>
      <td>3.663564</td>
      <td>5.993962</td>
      <td>3.367299</td>
      <td>-9.21034</td>
      <td>4.174389</td>
      <td>-9.21034</td>
      <td>-9.210340</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>4.189656</td>
      <td>-9.21034</td>
      <td>3.713575</td>
      <td>1.386319</td>
      <td>6.700875</td>
    </tr>
    <tr>
      <th>2</th>
      <td>803055</td>
      <td>9880624</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>4.052621</td>
      <td>5.036953</td>
      <td>6.431331</td>
      <td>-9.210340</td>
      <td>5.313206</td>
      <td>1.926451</td>
      <td>2.995737</td>
      <td>3.496511</td>
      <td>3.465739</td>
      <td>3.970464</td>
      <td>5.003947</td>
      <td>3.091047</td>
      <td>3.091047</td>
      <td>4.234108</td>
      <td>4.174389</td>
      <td>-9.21034</td>
      <td>2.772595</td>
      <td>2.564957</td>
      <td>3.610921</td>
      <td>6.208590</td>
      <td>3.496511</td>
      <td>-9.21034</td>
      <td>3.931828</td>
      <td>-9.21034</td>
      <td>4.553878</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>3.713575</td>
      <td>-9.21034</td>
      <td>3.610921</td>
      <td>-9.210340</td>
      <td>6.723034</td>
    </tr>
    <tr>
      <th>3</th>
      <td>803150</td>
      <td>9880652</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>4.228017</td>
      <td>4.615122</td>
      <td>6.527958</td>
      <td>-9.210340</td>
      <td>5.783825</td>
      <td>1.855688</td>
      <td>3.178058</td>
      <td>-9.210340</td>
      <td>3.295841</td>
      <td>3.667786</td>
      <td>-9.210340</td>
      <td>2.890377</td>
      <td>-9.210340</td>
      <td>4.043053</td>
      <td>4.143136</td>
      <td>-9.21034</td>
      <td>3.295841</td>
      <td>2.833219</td>
      <td>3.610921</td>
      <td>6.122493</td>
      <td>3.367299</td>
      <td>-9.21034</td>
      <td>3.555351</td>
      <td>-9.21034</td>
      <td>3.806665</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>4.060445</td>
      <td>-9.21034</td>
      <td>3.637589</td>
      <td>-9.210340</td>
      <td>6.727064</td>
    </tr>
    <tr>
      <th>4</th>
      <td>803070</td>
      <td>9880576</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>4.299163</td>
      <td>5.214936</td>
      <td>6.630684</td>
      <td>-9.210340</td>
      <td>5.525453</td>
      <td>2.032887</td>
      <td>3.806665</td>
      <td>4.248497</td>
      <td>-9.210340</td>
      <td>3.742731</td>
      <td>4.025353</td>
      <td>2.890377</td>
      <td>2.197236</td>
      <td>4.189656</td>
      <td>3.988986</td>
      <td>-9.21034</td>
      <td>2.890377</td>
      <td>2.708057</td>
      <td>3.688882</td>
      <td>6.272877</td>
      <td>3.555351</td>
      <td>-9.21034</td>
      <td>4.174389</td>
      <td>3.25810</td>
      <td>4.836283</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>-9.21034</td>
      <td>4.219509</td>
      <td>-9.21034</td>
      <td>3.433990</td>
      <td>-9.210340</td>
      <td>6.708392</td>
    </tr>
  </tbody>
</table>
</div>



Next, we will use `matplotlib` to define our canvas and axes and then loop into each element in our dataset to plot each histogram. 


```python
fig, ax = plt.subplots(nrows=7, ncols=5, figsize=(20,8), sharey=True)
plt.subplots_adjust(top=3)


row = 0
col = 0
for element in data.iloc[:,2:].columns:
    x=list(data[element])
    ax[row,col].hist(x, bins=35)
    ax[row,col].set_title("log " + element)
    if col<4:
        col+=1
    else:
        col=0
        row+=1
        
plt.show()
```


![png](/img/SS_data_summary_files/SS_data_summary_16_0.png)


Code above can be separated into two sections. The first section of the code will define the figure and axis canvas for our plot. Since we are dealing with 35 variables we will divide our subplots into 7 rows and 5 columns. 

We can check the length of our variable with:


```python
'''
it is getting annoying to keep typing data.iloc[:,2:] 
to get our elements so let's just put it into a
variable called grade
'''
grade = data.iloc[:,2:]
    
len(grade.columns)
```




    35



The second section of the code defines the loop behavior that will plot each histogram into predefined subplots.

## Correlation Matrix

Our next figure will be a correlation matrix. This is a very useful and neat graph that will tell us the correlation coefficient of one variable with another variable within the dataset. Correlation matrix value ranges from -1 to 1, where:
- -1 = perfect negative correlation 
- 0 = no correlation
- 1 = perfect positive correlation.

`Pandas` come in handy with its `corr()` function to calculate a correlation matrix of our dataset. Combine it with `matplotlib` functions such as: `matshow()` to draw the matrix into a figure; `cmap()` to denote it with colormap; and `colorbar()` to draw the legend, and we can get this informative graph.


```python
cor_matrix = grade.corr()
fig = plt.figure(figsize=(20, 18))
ax = fig.add_subplot(111)
cax = ax.matshow(cor_matrix,cmap='coolwarm', vmin=-1, vmax=1)
ticks = np.arange(0,len(grade.columns),1)

fig.colorbar(cax)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
plt.title('Correlation Matrix')
ax.set_yticks(ticks)
ax.set_xticklabels(grade.columns)
ax.set_yticklabels(grade.columns)

plt.show()
```


![png](/img/SS_data_summary_files/SS_data_summary_22_0.png)


## Map plots

With the same concept as the histograms plot, we can make quick and dirty map plots of our points to get a glimpse of the spatial correlation of each element. For this purpose we use `scatter()` function with our UTM coordinates as its x and y value and denote the concentration value of each element to a color map using `cmap()`. We do this using `for` loop so it can loop to each *element* in our `grade` data.


```python
fig, ax = plt.subplots(figsize=(20,50), nrows=12, ncols=3)

rows=0
cols=0 
for element in grade:
    cax = ax[rows,cols].scatter(data['EASTING'], data['NORTHING'], c=grade[element], cmap='coolwarm', s=10, alpha=0.9)
    ax[rows,cols].set_xticklabels('')
    ax[rows,cols].set_yticklabels('')
    ax[rows,cols].set_title(element)
    ax[rows,cols].axis('equal')
    fig.colorbar(cax, ax=ax[rows,cols])
    if cols<2:
        cols+=1
    else:
        cols = 0
        rows += 1
ax[11,2].set_axis_off()

plt.show()
```


![png](/img/SS_data_summary_files/SS_data_summary_25_0.png)


And that's it. Your soil sampling data summary in just about a minute. You can download the full code on my [GitHub page](https://github.com/nasirlukman/project-dump/tree/main) and reuse it for your next project. Hope it can save you the trouble and you can be more focused on your real geologist work. Have fun exploring!
