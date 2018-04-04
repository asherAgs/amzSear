## CLI

The amzSear CLI is the main entry point for using the amzSear package. It is similar to the [original version](../../legacy/v1) and backwards has been maintained where possible. However some features had to be changed consequently some CLI commands had to be changed, as discussed [below](#comparison-to-version-1).

The CLI, in it's basic form can still be used in the following way:

```
$ amzsear 'Harry Potter Books'
```

<a name="usage"></a>
##### Usage

The extended amzSear usage can be seen by typing `amzsear` without any additional arguments.

```
usage: amzsear [-h] [-p PAGE] [-i ITEM]
               [-r {AU,BR,CA,CN,DE,ES,FR,IN,IT,JP,MX,NL,SG,UK,US}] [-d]
               [-o {short,verbose,quiet,csv,json}]
               query
```

###### Args
*query*: The query string to search Amazon.

###### Optional Args
*-h*: Display extended help & usage information.  
*-p NUM, --page NUM*: The page number to be searched (defaults to 1).  
*-i NUM, --item NUM*: The item index to be displayed (relative to the page). If no item is specified, the entire page's products will be displayed.  
*-r STR, --region STR*: The amazon country/region to be searched (defaults to. For a list of countries to country code see the [region table](../regions.md).  
*-d, --dont-open*: Stop the page from opening in the default browser.  
*-o STR, --output STR*: The output type to be displayed (defaults to short). Output types are as follows:
* *short*: A concise view of the title, price summary and rating.
* *verbose*: The complete amzSear representation taken from the core api representation.
* *quiet*: No output is produced.
* *csv*: A quoted csv of all products with with all fields flattened, including the index.
* *json*: A Json object of all products with all fields with the product's index as the top-level key.

<a name="comparison-to-version-1"></a>
##### Comparison to Version 1

###### Verbose Argument
In the previous version of amzSear, a verbose option could be displayed by adding the `-v` argument. However this can now be done through the output argument. For example:
```
$ amzsear 'Harry Potter' --output verbose

OR

$ amzsear 'Harry Potter' -o verbose
```

###### Quiet Argument
Similar to the verbose argument, a quiet option could be used in the previous version of amzSear by adding the `-q` argument. However this can now be done through the output argument. For example:
```
$ amzsear 'Harry Potter' --output quiet

OR

$ amzsear 'Harry Potter' -o quiet
```

<a name="examples"></a>
##### Examples

###### Example 1
```
$ amzsear 'Harry Potter' -p 1

	OR

$ amzsear 'Harry Potter' --page 1
```
In the above example, the first page of results for the query `Harry Potter` will be displayed. The query `amzsear 'Harry Potter'` would have the same result as the default page number is 1.

###### Example 2
```
$ amzsear 'Harry Potter' -i 20

	OR

$ amzsear 'Harry Potter' --item 20
```
This example will display the item at index 20 of page 1 (as page 1 is the default). If the index could not be found on page 1 an empty result will appear.

###### Example 3
```
$ amzsear 'Harry Potter' -r ES

	OR
    
$ amzsear 'Harry Potter' --region ES
```
Example 3 will display all results from the `Harry Potter` searching the Spanish Amazon website. 

###### Example 4
```
$ amzsear 'Harry Potter' -d

	OR
    
$ amzsear 'Harry Potter' --dont-open
```
This example will produce the same output as it would without the `-d` option, however the page will not be opened in the default browser.

###### Example 5
```
$ amzsear 'Harry Potter' -o csv > harry_amzsear.csv

	OR
    
$ amzsear 'Harry Potter' --output csv > harry_amzsear.csv
```
In this example a csv of all products from the first page of search results is produced and then piped into a csv called `harry_amzsear.csv`.

###### Example 6
```
$ amzsear 'Harry Potter' -p 2 -i 35 --output json
```
In this final example a Json object of the item at index 35 on page 2 is displayed.



