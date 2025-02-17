class Main {

public static void main(String[]
args) {
System.out.println
("Inicializando...");
System.out.println("Car...");
Car car = new Car("AMQ123" , new 
Account("Andres Loaiza", 
"ADN1235", "andres1@hotmail.com", "12365"));
car.passenger = 4;
car.printDataCar();

System.out.println("Uberx...");
UberX uberx = new UberX
("MkL185", new Account("María Loyola", "JKL12365", "maria@hotmail.com", "125478"),
"Toyota", "Corolla");






}


}