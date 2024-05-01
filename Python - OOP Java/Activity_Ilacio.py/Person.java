public class Person {

    //Global variables
    private String name, status;
    private int age;
    private String nickname, vegetable, fruit, subject, teacher;

    
    //1st Constructors
    Person(String name, int age, String status){
        this.name = name;
        this.age = age;
        this.status = status; 
    }


    //Overload constructor
    Person(String nickname, String vegetable, String fruit, String subject, String teacher){
        this.nickname = nickname;
        this.vegetable = vegetable;
        this.fruit = fruit;
        this.subject = subject;
        this.teacher = teacher;
    }


    //Encapsulates access to private variables
    String getName(){
        return name;
    }

    String getStatus(){
        return status;
    }

    int getAge(){
        return age;
    }

    String getNickname(){
        return nickname;
    }

    String getVegetable(){
        return vegetable;
    }

    String getFruit(){
        return fruit;
    }

    String getSubject(){
        return subject;
    }

    String getTeacher(){
        return teacher;
    }
}
