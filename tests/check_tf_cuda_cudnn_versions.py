# ---------------------------------------------------------------------------- #
#                                   Test Unit                                  #
# ---------------------------------------------------------------------------- #

import tensorflow as tf


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


if __name__ == "__main__":
    get_gpu_info()
