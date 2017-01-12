# HUB25 - Machine Learning
## Icebreaker Exercise Material

#### The Script
Generates distributions of training and test datapoints for two groups, produces SVGs of the cards laid out 10 per page, and creates a `bokeh` plot of the distributions for viewing.

```
python card_layout.py
```

Requires: `bokeh`, `matplotlib`, and `numpy`.

The cards used in the original exercise at HUB are available as PDFs in this directory.

#### The Cards
The PDFs in this directory are layouts of cards with colored numbers, which can be used as test and training data for a classsification problem. The 'training' cards display a single 'data point', with values in two dimension - an integer in a range of roughly 1-100 and a colour along a spectrum from blue to red.

#### The Exercise
The idea behind the icebreaker exercise was to provide HUB attendees as 'data points' to a smaller group of sttendees who would act as a 'classifier' in a supervised learning problem. The attendees are divided into three groups - one small group (4 or 5 people) would act as the 'classifier', while the remaing people would be divided roughly equally into the other two groups - the test and training 'data'.

Each member of the test and training groups was given a card, drawn from the appropriate set. The training data then present themselves to the classifier group for 'learning' within a short time period (5-10 mins). After the classifier group is happy that they have learned from the training data (or they run out of time), the test data present themselves for classification, and are assigned to one group or the other by the classifiers.

After the 'classification' is finished, the test data points can see whether they hae been assigned to the correct group by checking the second position in the hash key on their card - an odd number (1, 3, 5) in the second position means that they originate from group 1, while an even number (0, 2, 4) in the second position indicates membership of group 2.
