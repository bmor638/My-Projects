# Principal Component Analysis on Two Wheels
#   Exploring dimensionality reduction with cycling data in R

knitr::opts_chunk$set(echo = TRUE)
library(tidyverse)
library(readxl)
library(tidyr)
library(ggpubr)
library(reshape2)
library(plotly)

# DATA


# ===read and review data===
# read data from Excel file
dat<-read_excel("DATA.xlsx", sheet="1.ALL DATA FOR MODELS")

# display data dimensions
cat("Dimensions: ", dim(dat), "\n\n")

# compute male/female proportions
print("Gender proportions:")
table(dat$Gender)/nrow(dat)

# display age range
cat("Age range: ", range(dat$Age), "\n\n")


# APPLICATION


# ====pre-processing====
# restrict to continuous variables
dat<-dat%>%select(Age, Height, Bodymass, Frequency_cycling, Hours_week_cycling, Km_week, TOTALKM, Experience, Speed)


# ====PCA====
# apply PCA to the training data, centering and scaling to standardize the features
pc<-prcomp(dat, center=TRUE, scale.=TRUE)

# view the attributes of the PCA object, including the standard deviations of the principal components and the rotation matrix (loadings)
# attributes(pc)

# view the proportion of variance explained by each principal component
# print(pc)

# view the summary of the PCA (shortened to 3 PCs), including the cumulative proportion of variance explained by the principal components 
summary(pc)$importance[,1:3]

# ===visualizations===
# scree plot
# create a data frame with each PC and its corresponding variance explained and cumulative variance explained
eig_df<-data.frame(
  PC=1:length(pc$sdev),
  eigenvalue=pc$sdev^2,
  variance=(pc$sdev^2)/sum(pc$sdev^2),
  cum=cumsum((pc$sdev^2)/sum(pc$sdev^2))
)

ggplot(eig_df, aes(PC, eigenvalue)) +
  geom_line() +
  geom_point() +
  labs(
    title="Scree Plot: Eigenvalues of Principal Components",
    x="Principal Component",
    y="Eigenvalue"
  ) +
  scale_x_continuous(breaks=1:10)

# cumulative variance explained plot, with purple lines for 70% variance explained
ggplot(eig_df, aes(x=PC, y=cum)) +
  geom_line() +
  geom_point() +
  geom_hline(yintercept=0.7, color="purple") +
  geom_vline(xintercept=which(eig_df$cum>=0.7)[1], color="purple") +
  labs(
    title="Cumulative Proportion Variance Explained 
by Principal Components",
    x="Principal Component",
    y="Cumulative Proportion of Variance Explained"
  ) +
  scale_x_continuous(breaks=1:10)

# ===decide number of PCs to retain===
# for 70% cumulative variance explained
num_pcs_70<-which(eig_df$cum >= 0.7)[1]
num_pcs_70

# for 90% cumulative variance explained
num_pcs_90<-which(eig_df$cum >= 0.9)[1]
num_pcs_90

# ===decide number of PCs to retain===
# Kaiser criterion
(num_pcs<-sum(pc$sdev^2 > 1))

# check the eigenvalues of the first 'num_pcs+3' PCs
eigenvalues<-pc$sdev^2
print("PC eigenvalues:")
eigenvalues

# ===extract the first 'num_pcs' PCs===
predictors<-pc$x[,1:num_pcs]

# ===PC space projections===
# create data frames for plotting
pca_df <- data.frame(
  PC1 = pc$x[,1],
  PC2 = pc$x[,2],
  Km_week = dat$Km_week
)

pca_3d_df <- data.frame(
  PC1 = pc$x[,1],
  PC2 = pc$x[,2],
  PC3 = pc$x[,3],
  Km_week = dat$Km_week
)

# 2D scatter plot
ggplot(pca_df, aes(PC1, PC2, color=Km_week)) +
  geom_point(alpha=0.6, size=2) +
  labs(
    title="Cyclists in the PC1 x PC2 space",
    x="PC1",
    y="PC2",
    color="Training km/week"
  ) +
  scale_color_gradient(low="blue", high="red")

# 3D scatter plot
p<-plot_ly(pca_3d_df, 
           x=~PC1, 
           y=~PC2, 
           z=~PC3,
           color=~Km_week,
           colors=colorRamp(c("blue", "red")),
           type="scatter3d",
           mode="markers",
           marker=list(size=3, opacity=0.6))%>%layout(scene=list(
             xaxis=list(title="PC1"),
             yaxis=list(title="PC2"),
             zaxis=list(title="PC3")),
             title="Cyclists in 3D PC Space")

# display 3D plot
#p

# find the top 2 variables by absolute loading, keeping the sign
loadings<-pc$rotation[,1:num_pcs]
top_loadings_signed<-apply(loadings, 2, function(x) {
  top_idx<-order(abs(x), decreasing=TRUE)[1:2]   # indices of top 2 variables by absolute value
  paste(names(x)[top_idx], sprintf("(%.2f)", x[top_idx]))  # include loading values
})

print("Top 2 variables contributing to each PC:")
top_loadings_signed
