# ---------------------------------------------------------------------------- #
#                      Authored by Matheus Ferreira Silva                      #
#                           github.com/MatheusFS-dev                           #
# ---------------------------------------------------------------------------- #    

import tensorflow as tf
import os

def get_gpu_info():
    """
    Retrieves and prints detailed GPU information including TensorFlow,
    CUDA, cuDNN versions, number of GPUs, and memory details.
    """
    # Display TensorFlow version
    print(f"TensorFlow Version: {tf.__version__}")

    # Check if TensorFlow is built with CUDA support and retrieve build info
    if tf.test.is_built_with_cuda():
        build_info = tf.sysconfig.get_build_info()
        print(f"TensorFlow is built with CUDA support")
        print(f"CUDA Version: {build_info['cuda_version']}")
        print(f"cuDNN Version: {build_info['cudnn_version']}")
    else:
        print("Running on CPU (No CUDA support detected)")

    # Detect available GPUs
    gpus = tf.config.list_physical_devices("GPU")
    if gpus:
        print(f"\nNumber of GPUs detected: {len(gpus)}")
        print(f"Available GPU(s): {[gpu.name for gpu in gpus]}\n")
        tf.test.gpu_device_name()
    else:
        print("No GPUs found")
        print("Running on CPU")

def enable_memory_growth():
    """
    Enables memory growth for all detected GPUs.
    """
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        for i, gpu in enumerate(gpus):
            try:
                tf.config.experimental.set_memory_growth(gpu, True)
                print(f"Memory growth enabled for GPU {i}: {gpu.name}")
            except RuntimeError as e:
                print(f"Error enabling memory growth for GPU {i}: {gpu.name}, {e}")

if __name__ == "__main__":
    # Specify GPU to use (e.g., GPU 0)
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    
    get_gpu_info()
    enable_memory_growth()
