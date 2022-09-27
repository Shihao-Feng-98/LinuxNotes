# C/C++ development based on VSCode and CMake
Reference: [C/C++ development based on VSCode and CMake](https://github.com/Shihao-Feng-98/Linux_notes/blob/main/cpp_vscode/%E5%9F%BA%E4%BA%8EVSCode%E5%92%8CCMake%E5%AE%9E%E7%8E%B0C%2B%2B%E5%BC%80%E5%8F%91%20-%20Linux%E7%AF%87V1.0.pdf)

## g++ direct compile
only main.cpp file

```
g++ main.cpp -o main
```

include head files (`include`) and source files (`src`)
```
g++ main.cpp src/source1.cpp src/source2.cpp -Iinclude -o main
```

## CMake compile
write `CMakeLists.txt` file, the minmum cmake file see 
