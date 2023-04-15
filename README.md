# FDP - A PDF Programming language

FDP is a programming language created to make PDF text extraction easy. The motivation was found when i noticed that all the companies that must deal with PDFs has to write their own complex code to extract different kinds of PDFs. This requires a lot of effort and time to write and test.

With FDP, you can write a very easy and simple file with instructions of where to find the data inside the PDF, and the language's core will take care of the rest

## Syntax examples:
```
FROM path/to/file.pdf

car_model -> after "the car model is: " before "model year"
year -> after "model year: " before "additional details"
```
```
> fdp fdp_file.fdp
< {
    "car_model": "Civic 10th Generation",
    "year": "2017"
  }

```

## Build steps
Install with PIP
```
pip3 install git+https://github.com/gustavo-bordin/fdp.git
```