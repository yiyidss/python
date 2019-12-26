# 笔记
- 包导入的时候，导入的是文件名，文件名导入时不合法的时候使用importlib，例如01.py
    
        import importlib
        module_name = importlib.import_module("01")
        module_name.fun_name()   # 使用01模块中的方法
- 被导入时，不想让其他模块使用的方法

        if __name__ == "__main__":
            func...
        例如10,11
- 导入包
    - import package_name
    
            使用__init__.py文件，在此文件导入包中的模块
    - import package.module
        
            直接导入包中的某一具体模块
    - from package import module
    
            此种方法不执行__init__的内容
    - from package import *
            
            如果设置了__all__，则按照__all__里的模块载入，不载入__init__文件的其他内容
            __all__ = [module_name,...]