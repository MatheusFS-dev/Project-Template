import tensorflow as tf

# Check TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

# Check if CUDA is available and its version
if tf.test.is_built_with_cuda():
    print("TensorFlow is built with CUDA support")
    
    # Check the CUDA version being used
    cuda_version = tf.sysconfig.get_build_info()['cuda_version']
    print(f"CUDA version: {cuda_version}")
    
    # Check the cuDNN version being used
    cudnn_version = tf.sysconfig.get_build_info()['cudnn_version']
    print(f"cuDNN version: {cudnn_version}")
else:
    print("TensorFlow is running on CPU (No CUDA detected)")
