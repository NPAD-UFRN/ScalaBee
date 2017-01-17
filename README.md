
# ScalaBee <img src="https://github.com/danielholanda/ScalaBee/blob/master/media/Bee?raw=true" width="35">
A simple automated scalability test environment designed for your computer or cluster

## Sample Output
![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/sampleOutputGraph.png?raw=true)![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/sampleOutputTable.png?raw=true)


## How to Use
### Usage
* Arguments
 

    ```bash
    scalaBee.py [+h] [+nTe numberOfTests] Prog Arg [Arg ...]
    ```
### Examples
* Generic example:

    Let's say your program has the arguments strutured like this:
    
    ```bash
    myProgram -numberOfThreads=X -problemSize=Y -otherArg=file.txt
    ```
    In this example, if you want to use 8 threads and the problem size is 10 you would execute
    
    ```bash
    myProgram -numberOfThreads=8 -problemSize=10 -otherArg=file.txt
    ```
    
    Now let's say you want to check this program's speedup and efficiency with 1, 2, 4, 8, 16 threads and with problem sizes 10, 100, 1000. To do this using Scalabee, simply type
    
    ```bash
    scalaBee.py myProgram -numberOfThreads={t16} -problemSize={p{10,100,1000}} -otherArg=file.txt
    ```
    
    If you want to run each combination multiple times to get a better time average (let's say 20 times) simply add the option:
    
    ```bash
    +nTe 20 
    ```
    Also note that it is optional to indicate the problem size.

## Dependencies 
* This project depends on Matplotlib and PrettyTable. To install them, use the command:

    ```bash
    pip install PrettyTable matplotlib
    ```

## Bug Reports & Feature Requests
You can help by reporting bugs, suggesting features, reviewing feature specifications or just by sharing your opinion.
Use [GitHub Issues](https://github.com/TheFighters/Smith-Waterman/issues) for all of that.


## Contributing
1. Fork the project.
2. Create a branch for your new feature.
3. Test your code.
5. Submit a pull request.

All pull requests are welcome !

## Authors
This project was develloped by [Daniel Holanda](https://github.com/danielholanda/).

## License
This project uses the MIT license. See [LICENSE](https://github.com/danielholanda/ScalaBee/blob/master/LICENSE) for more details.

