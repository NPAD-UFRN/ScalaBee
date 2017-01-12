# ScalaBee ![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/Bee?raw=true)
A simple automated scalability test environment designed for your computer or cluster



## Sample Output
![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/sampleOutputGraph.png?raw=true)![Demo Doccou alpha](https://github.com/danielholanda/ScalaBee/blob/master/media/sampleOutputTable.png?raw=true)


## How to Use
### On your local machine
* Arguments:
    
    ```bash
    python scalaBee.py numerOfTests program arg1Init-arg1Final arg2Init-arg2Final...
    ```
* Example:
    
    ```bash
    python scalaBee.py 2 ./examples/omp_pi 1,2,4,8,16 100000,1000000,10000000,100000000
    ```

### On a cluster
* This feature is still being develloped

## Dependencies 
* This project depends on Matplotlib and PrettyTable. To install them, use the command:
    ```bash
    pip install PrettyTable, matplotlib
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
