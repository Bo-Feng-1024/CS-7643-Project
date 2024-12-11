
#-----------------------------------------------------------------------------------
#   model accuracy in-domain vs out-of-domain (opt - 125m)
#-----------------------------------------------------------------------------------

#plot in-domain accuracy vs out-of-domain accuracy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame from clipboard
df = pd.read_clipboard()

# Calculate the average for each 'n'
avg_df = df.groupby('n').mean().reset_index()

# Define a color palette
palette = {2: 'red', 32: 'blue', 128: 'black'}

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='in_domain_accuracy', y='out_of_domain_accuracy', hue='n', palette=palette, data=avg_df, s=100)

# Plot the 45-degree line
max_val = max(avg_df['in_domain_accuracy'].max(), avg_df['out_of_domain_accuracy'].max())
plt.plot([0, 1], [0, 1], color='black', linestyle='--', alpha = 0.5)

# Add labels and title
plt.xlabel('In-Domain Accuracy')
plt.ylabel('Out-of-Domain Accuracy')
plt.title('Scatter Plot of Accuracies (opt - 125m)')

plt.legend(title='sample size')
# Show plot
plt.show()

#-----------------------------------------------------------------------------------
#   model loss in-domain vs out-of-domain (opt - 125m)
#-----------------------------------------------------------------------------------

#plot in-domain loss vs out-of-domain loss
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame from clipboard
df = pd.read_clipboard()

# Calculate the average for each 'n'
avg_df = df.groupby('n').mean().reset_index()

# Define a color palette
palette = {2: 'red', 32: 'blue', 128: 'black'}

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='in_domain_loss', y='out_of_domain_loss', hue='n', palette=palette, data=avg_df, s=100)

# Plot the 45-degree line
max_val = [avg_df['in_domain_loss'].max(), avg_df['out_of_domain_loss'].max()]
plt.plot([0, max_val[0]], [0, max_val[1]], color='black', linestyle='--', alpha = 0.5)

# Add labels and title
plt.xlabel('In-Domain loss')
plt.ylabel('Out-of-Domain loss')
plt.title('Scatter Plot of Model Loss (opt - 125m)')

plt.legend(title='sample size')
# Show plot
plt.show()



#-----------------------------------------------------------------------------------
#   model accuracy in-domain vs out-of-domain (opt - 350m)
#-----------------------------------------------------------------------------------

#plot in-domain accuracy vs out-of-domain accuracy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame from clipboard
df = pd.read_clipboard()

# Calculate the average for each 'n'
avg_df = df.groupby('n').mean().reset_index()

# Define a color palette
palette = {2: 'red', 32: 'blue', 128: 'black'}

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='in_domain_accuracy', y='out_of_domain_accuracy', hue='n', palette=palette, data=avg_df, s=100)

# Plot the 45-degree line
max_val = max(avg_df['in_domain_accuracy'].max(), avg_df['out_of_domain_accuracy'].max())
plt.plot([0, 1], [0, 1], color='black', linestyle='--', alpha = 0.5)

# Add labels and title
plt.xlabel('In-Domain Accuracy')
plt.ylabel('Out-of-Domain Accuracy')
plt.title('Scatter Plot of Accuracies (opt - 350m)')

plt.legend(title='sample size')
# Show plot
plt.show()

#-----------------------------------------------------------------------------------
#   model loss in-domain vs out-of-domain (opt - 350m)
#-----------------------------------------------------------------------------------

#plot in-domain loss vs out-of-domain loss
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame from clipboard
df = pd.read_clipboard()

# Calculate the average for each 'n'
avg_df = df.groupby('n').mean().reset_index()

# Define a color palette
palette = {2: 'red', 32: 'blue', 128: 'black'}

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='in_domain_loss', y='out_of_domain_loss', hue='n', palette=palette, data=avg_df, s=100)

# Plot the 45-degree line
max_val = [avg_df['in_domain_loss'].max(), avg_df['out_of_domain_loss'].max()]
plt.plot([0, max_val[0]], [0, max_val[1]], color='black', linestyle='--', alpha = 0.5)

# Add labels and title
plt.xlabel('In-Domain loss')
plt.ylabel('Out-of-Domain loss')
plt.title('Scatter Plot of Model Loss (opt - 350m)')

plt.legend(title='sample size')
# Show plot
plt.show()


#-----------------------------------------------------------------------------------
#   model loss vs learning rate (opt - 125m)
#-----------------------------------------------------------------------------------

#plot in-domain loss vs out-of-domain loss
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame from clipboard
df = pd.read_clipboard()

# Calculate the average for each 'n'
avg_df = df.groupby(['learning_rate', 'n']).mean().reset_index()

# Create a new column that combines 'n' and 'learning_rate'
avg_df['n_learning_rate'] = 'n = ' + avg_df['n'].astype(str) + ', learning rate = ' + avg_df['learning_rate'].astype(str)

# Define a color palette
unique_combinations = avg_df['n_learning_rate'].unique()
palette = dict(zip(unique_combinations, sns.color_palette("hsv", len(unique_combinations))))

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='in_domain_accuracy', y='out_of_domain_accuracy', hue='n_learning_rate', palette=palette, data=avg_df, s=100)

# Plot the 45-degree line
max_val = [avg_df['in_domain_accuracy'].max(), avg_df['out_of_domain_accuracy'].max()]
plt.plot([0, 1], [0, 1], color='black', linestyle='--', alpha = 0.5)

# Add labels and title
plt.xlabel('In-Domain accuracy')
plt.ylabel('Out-of-Domain accuracy')
plt.title('Comparison of Model Accuracy under Different Learning Rate (opt - 125m)')

plt.legend(title='sample size')
# Show plot
plt.show()


#-----------------------------------------------------------------------------------
#   model loss vs learning rate (opt - 125m)
#-----------------------------------------------------------------------------------

#plot in-domain loss vs out-of-domain loss
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read DataFrame from clipboard
df = pd.read_clipboard()

# Calculate the average for each 'n'
avg_df = df.groupby(['learning_rate', 'n']).mean().reset_index()

# Create a new column that combines 'n' and 'learning_rate'
avg_df['n_learning_rate'] = 'n = ' + avg_df['n'].astype(str) + ', learning rate = ' + avg_df['learning_rate'].astype(str)

# Define a color palette
unique_combinations = avg_df['n_learning_rate'].unique()
palette = dict(zip(unique_combinations, sns.color_palette("hsv", len(unique_combinations))))

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='in_domain_loss', y='out_of_domain_loss', hue='n_learning_rate', palette=palette, data=avg_df, s=100)

# Plot the 45-degree line
max_val = [avg_df['in_domain_loss'].max(), avg_df['out_of_domain_loss'].max()]
plt.plot([0, max_val[0]], [0, max_val[1]], color='black', linestyle='--', alpha = 0.5)

# Add labels and title
plt.xlabel('In-Domain loss')
plt.ylabel('Out-of-Domain loss')
plt.title('Comparison of Model Loss under Different Learning Rate (opt - 125m)')

plt.legend(title='sample size')
# Show plot
plt.show()

