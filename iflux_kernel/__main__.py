if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    from iflux_kernel.kernel import IFluxKernel
    IPKernelApp.launch_instance(kernel_class=IFluxKernel)
