package com.boxinbox.baradhotest;

import javafx.application.Application;
import javafx.stage.Stage;

import java.io.IOException;

import com.boxinbox.baradho.Baradho;

/**
 * JavaFX App
 */
public class App extends Application {

    Baradho baradho;

    @Override
    public void start(Stage stage) throws IOException {
        System.out.println("start");
        baradho = new Baradho(stage, this, new Test());
    }

    public static void main(String[] args) {
        launch();
    }

}