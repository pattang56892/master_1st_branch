using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/aFriend", () =>
{
    string aFriend = "Bill";
    return aFriend;
});

app.MapGet("/greeting", () =>
{
    string greeting = "Hello World - Greeting!";
    return greeting;
});

app.MapGet("/multipleStatements", () =>
{
    string aFriend = "Bill";
    string firstFriend = "Maria";
    string secondFriend = "Sage";
    string greeting = "      Hello World!       ";
    string sayHello = "Hello World!";
    string songLyrics = "You say goodbye, and I say hello";

    string result = $"{aFriend}\n" +
                    $"Hello {aFriend}\n" +
                    $"My friends are {firstFriend} and {secondFriend}\n" +
                    $"The name {firstFriend} has {firstFriend.Length} letters.\n" +
                    $"The name {secondFriend} has {secondFriend.Length} letters.\n" +
                    $"[{greeting}]\n" +
                    $"[{greeting.TrimStart()}]\n" +
                    $"[{greeting.TrimEnd()}]\n" +
                    $"[{greeting.Trim()}]\n" +
                    $"{sayHello}\n" +
                    $"{sayHello.Replace("Hello", "Greetings")}\n" +
                    $"{sayHello.ToUpper()}\n" +
                    $"{sayHello.ToLower()}\n" +
                    $"{songLyrics.Contains("goodbye")}\n" +
                    $"{songLyrics.Contains("greetings")}\n" +
                    $"{songLyrics.StartsWith("You")}\n" +
                    $"{songLyrics.StartsWith("goodbye")}\n" +
                    $"{songLyrics.EndsWith("hello")}\n" +
                    $"{songLyrics.EndsWith("goodbye")}\n";

    return result;
});

app.Run();

var host = builder.Build();
host.Run();
