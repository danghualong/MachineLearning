using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace InteractiverConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            ScriptEngine engine = Python.CreateEngine();
            ScriptScope scope = engine.CreateScope();
            //Student stu = new Student("LiLei", 30);
            //scope.SetVariable("stu", stu);
            ScriptSource src = engine.CreateScriptSourceFromFile("drawer.py");
            src.Execute(scope);

            //ScriptRuntime runtime = Python.CreateRuntime();
            //var stu = new Student("LiLei", 30);
            //dynamic module=runtime.UseFile("drawer.py");
            //var m = new int[3] { 1, 2, 3 };
            //module.printStu(m);


            Console.ReadKey();
        }
    }

    public class Student
    {
        public Student(string name, int age)
        {
            this.Name = name;
            this.Age = age;
        }

        public string Name
        {
            get; set;
        }
        public int Age
        {
            get; set;
        }
    }
}
