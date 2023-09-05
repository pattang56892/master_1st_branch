using System.Data.SQLite;
using System.IO;

public static class DatabaseHelper
{
    private static string connectionString = @"Data Source=..\..\Files\LibraryManagementSystem.db;Version3;";

    public static void InitializaDatabase()
    {
        if (!File.Exists(@"..\..\Files\LibraryManagementSyetem.db"))
        {
            SQLiteConnection.CreateFile(@"..\..\Files\LiabraryManagementSystem.db");

                using (var connection = new SQLiteConnection(connectionString))
                {

                    connection.Open();

                    // Create tables for your data
                    string createBooksTableQuery = @"
                        CREATE TABlE IF NOT EXISTS books (
                        id  INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT NOT NULL
                        );";

                    string createUsersTableQuery = @"
                        CREATE TABlE IF NOT EXISTS users (
                        id  INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        user_type TEXT NOT NUll
                        );";

                using (var command = new SQLiteCommand(connection))
                {
                    command.CommandText = createBooksTableQuery;
                    command.ExecuteNonQuery();

                    command.CommandText = createUsersTableQuery;
                    command.ExecuteNonQuery();
                }
            }
        }
    }
}

