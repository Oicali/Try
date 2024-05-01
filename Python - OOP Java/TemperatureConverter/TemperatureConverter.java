public class TemperatureConverter {
    public static void main(String []args){

        convertToFarenheit Celsius = new convertToFarenheit(6);
        System.out.format("%.2f", Celsius.ToFahrenheit());

        System.out.println();

        convertToCelsius Farenheit = new convertToCelsius(6);
        System.out.format("%.2f", Farenheit.ToCelsius());
    }
}

class convertToFarenheit{
    double celsiusVal;

    //constructors
    convertToFarenheit(double Celsius){
        this.celsiusVal = Celsius;
    }

    //Method for the conversion
    public double ToFahrenheit(){
        return (celsiusVal * 1.8) + 32;
    }
}

class convertToCelsius{
    double farenheitVal;

    //constructors
    convertToCelsius(double Farenheit){
        this.farenheitVal = Farenheit;
    }

    //Method for the conversion
    public double ToCelsius(){
        return (farenheitVal - 32) / 1.8;
    }
}
