class ComputeKelvin {
    private double x;

    public ComputeKelvin() {
        x = 37;
    }

    public ComputeKelvin(double value) {
        x = value;
    }

    public double calculateKelvin() {
        return x + 273.15;
    }
}

class ComputeFahrenheit {
    private double x;

    public ComputeFahrenheit() {
        x = 37;
    }

    public ComputeFahrenheit(double value) {
        x = value;
    }

    public double calculateFahrenheit() {
        return x * 1.8 + 32;
    }
}

public class Main {
    public static void main(String[] args) {
        ComputeFahrenheit fahrenheitDefault = new ComputeFahrenheit();
        double fahrenheitDefaultVal = fahrenheitDefault.calculateFahrenheit();
        System.out.println("The fahrenheit using default constructor is value is " + fahrenheitDefaultVal);

        ComputeFahrenheit fahrenheitUser = new ComputeFahrenheit(10);
        double fahrenheitUserVal = fahrenheitUser.calculateFahrenheit();
        System.out.println("The fahrenheit using the user defined value is " + fahrenheitUserVal);

        ComputeKelvin kelvinDefault = new ComputeKelvin();
        double kelvinDefaultVal = kelvinDefault.calculateKelvin();
        System.out.println("The Kelvin using the constructor value is " + kelvinDefaultVal);

        ComputeKelvin kelvinUser = new ComputeKelvin(20);
        double kelvinUserVal = kelvinUser.calculateKelvin();
        System.out.println("The kelvin using user defined value is " + kelvinUserVal);
    }
}
