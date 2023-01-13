import 'package:flutter/material.dart';

void main(List<String>) {
    runApp(MyApp());
}

class MyApp extends StatelessWidget {
    // const ({ key? key }) : super(key: key);

    @override
    Widget build(BuildContext context){
        return MaterialApp(
            home: text("COVID CHECKER"),
        ); //MaterialApp
    }
}