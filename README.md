
# ScalaBee <img src="https://github.com/danielholanda/ScalaBee/blob/master/media/Bee?raw=true" width="35">
A simple automated scalability test environment designed for your computer or cluster

## Sample Output
![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/sampleOutputGraph.png?raw=true)![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/sampleOutputTable.png?raw=true)


## How to Use
### On your local machine
* Usage: 

    ```bash
    python scalaBee.py [+h] [+nTe numberOfTests] Prog Arg [Arg ...]
    ```
* Example:

    Let's say your program has the arguments strutured like this:
    
    ```bash
    myProgram numberOfThreads problemSize
    ```
    
    You can use scalaby to test it with 1, 2, 4, 8, 16 threads and with problem size 100000, 1000000, 10000000, 100000000 by simply running.
    
    ```bash
    python scalaBee.py myProgram {t16} {p{100000,1000000,10000000,100000000}}
    ```
    
    You can also run each combination 10 times, for example. For this, simply add the option:
    
    ```bash
    +nTe 10 
    ```

### On a cluster
* This feature is still being developed

## Dependencies 
* This project depends on Matplotlib and PrettyTable. To install them, use the command:

    ```bash
    pip install PrettyTable matplotlib
    ```

## Bug Reports & Feature Requests
You can help by reporting bugs, suggesting features, reviewing feature specifications or just by sharing your opinion.
Use [GitHub Issues](https://github.com/TheFighters/Smith-Waterman/issues) for all of that.

## To do
* Add cluster support
* Change the way that the inputs are received for a more flexible use
    
    
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
