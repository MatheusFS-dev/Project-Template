"""
# --------------------------------------------------------------------------- #
# Module: gpu_info.py
# Purpose: Detect and display GPU, CUDA, and TensorFlow details.
# 
# Author: Matheus Ferreira Silva
# GitHub: https://github.com/MatheusFS-dev
# Created: 2024-12-19
# Last Modified: 2024-12-19
# Dependencies: TensorFlow
# --------------------------------------------------------------------------- #
"""

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
        print("Running on CPU (No CUDA support detected).")

    # Detect available GPUs
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"Number of GPUs detected: {len(gpus)}")
        print(f"Available GPU(s): {[gpu.name for gpu in gpus]}")
        for i, gpu in enumerate(gpus):
            # Get GPU details using logical device configuration
            details = tf.config.experimental.get_device_details(gpu)

            memory_info = tf.config.experimental.get_memory_info(gpu.name)
            print(f"GPU {i} Details:")
            print(f"  Name: {details.get('device_name', 'Unknown')}")
            print(f"  Total Memory: {memory_info.get('total', 'Unknown')} bytes")
            print(f"  Free Memory: {memory_info.get('free', 'Unknown')} bytes")

        print(f"Using GPU: {tf.test.gpu_device_name()}")
    else:
        print("No GPUs found. Running on CPU.")

def enable_memory_growth():
    """
    Enables memory growth for all detected GPUs.
    """
    # Specify GPU to use (e.g., GPU 0)
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        for i, gpu in enumerate(gpus):
            try:
                tf.config.experimental.set_memory_growth(gpu, True)
                print(f"Memory growth enabled for GPU {i}: {gpu.name}")
            except RuntimeError as e:
                print(f"Error enabling memory growth for GPU {i}: {gpu.name}, {e}")

if __name__ == "__main__":
    get_gpu_info()
    enable_memory_growth()
