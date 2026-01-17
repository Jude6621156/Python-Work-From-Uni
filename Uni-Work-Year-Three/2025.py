import numpy as np
import matplotlib.pyplot as plt

# Function to create nice-looking tables for visualization
def plot_matrix(matrix, title, subplot_pos=None, colormap='coolwarm', show_values=True):
    if subplot_pos:
        plt.subplot(subplot_pos)
    plt.imshow(matrix, cmap=colormap)
    plt.title(title)
    plt.colorbar()
    
    # Add value annotations
    if show_values:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                plt.text(j, i, f'{matrix[i, j]:.1f}', 
                        ha='center', va='center', 
                        color='white' if abs(matrix[i, j]) > 2 else 'black')
    
    plt.axis('tight')

# 1. Original Input and Kernel
input_matrix = np.array([
    [7, 4, 6, 2],
    [3, 1, 1, 5],
    [0, 1, 0, 0],
    [0, 8, 5, 3]
])

kernel = np.array([
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
])

# 2. Padding function
def add_padding(matrix, pad_width):
    return np.pad(matrix, pad_width, mode='constant', constant_values=0)

# 3. Convolution function
def convolve2d(input_matrix, kernel, stride=1, padding=1):
    # Add padding
    padded = add_padding(input_matrix, padding)
    
    # Get dimensions
    kernel_height, kernel_width = kernel.shape
    padded_height, padded_width = padded.shape
    
    # Calculate output dimensions
    output_height = ((padded_height - kernel_height) // stride) + 1
    output_width = ((padded_width - kernel_width) // stride) + 1
    
    # Initialize output
    output = np.zeros((output_height, output_width))
    
    # Perform convolution
    for i in range(0, padded_height - kernel_height + 1, stride):
        for j in range(0, padded_width - kernel_width + 1, stride):
            window = padded[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(window * kernel)
            
    return output

# 4. Average pooling function
def average_pooling(matrix, pool_size=2):
    height, width = matrix.shape
    pooled_height = height // pool_size
    pooled_width = width // pool_size
    
    output = np.zeros((pooled_height, pooled_width))
    
    for i in range(pooled_height):
        for j in range(pooled_width):
            window = matrix[i*pool_size:(i+1)*pool_size, 
                          j*pool_size:(j+1)*pool_size]
            output[i, j] = np.mean(window)
            
    return output

# Create visualizations
plt.figure(figsize=(15, 10))

# Original input
plot_matrix(input_matrix, 'Original Input (4x4)', 231)

# Kernel
plot_matrix(kernel, 'Kernel (3x3)', 232)

# Padded input
padded_input = add_padding(input_matrix, 1)
plot_matrix(padded_input, 'Padded Input (6x6)', 233)

# Convolution output
conv_output = convolve2d(input_matrix, kernel)
plot_matrix(conv_output, 'Convolution Output (4x4)', 234)

# Average pooling output
pooled_output = average_pooling(input_matrix)
plot_matrix(pooled_output, 'Average Pooling Output (2x2)', 235)

plt.tight_layout()
plt.show()

# Print numerical results
print("\nPadded Input:")
print(padded_input)
print("\nConvolution Output:")
print(conv_output)
print("\nAverage Pooling Output:")
print(pooled_output)
