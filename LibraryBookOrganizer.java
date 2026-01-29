import java.util.Scanner;

public class LibraryBookOrganizer {

    // Method to take book input from user
    public static String[][] inputBooks(int n) {
        Scanner sc = new Scanner(System.in);
        String[][] books = new String[n][2]; // 2D array: [title][author]

        System.out.println("Enter book details (Title and Author):");
        for (int i = 0; i < n; i++) {
            System.out.print("Enter title of book " + (i + 1) + ": ");
            books[i][0] = sc.nextLine().trim(); // String method: trim()

            System.out.print("Enter author of book " + (i + 1) + ": ");
            books[i][1] = sc.nextLine().trim();
        }
        return books;
    }

    // Method to search books by author
    public static void searchByAuthor(String[][] books, String author) {
        boolean found = false;
        author = author.trim().toLowerCase(); // String methods used

        System.out.println("\nBooks by " + author + ":");
        for (int i = 0; i < books.length; i++) { // loop using array length
            if (books[i][1].toLowerCase().equals(author)) {
                System.out.println("- " + books[i][0]);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No books found for this author.");
        }
    }

    // Method to display all books
    public static void displayAllBooks(String[][] books) {
        System.out.println("\nAll Books in Library:");
        for (int i = 0; i < books.length; i++) {
            System.out.println((i + 1) + ". " + books[i][0] + " - " + books[i][1]);
        }
    }

    // Main method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 2D array with 5 books
        int totalBooks = 5;
        String[][] books = inputBooks(totalBooks);

        // Display all books
        displayAllBooks(books);

        // Search by author
        System.out.print("\nEnter author name to search: ");
        String author = sc.nextLine();

        searchByAuthor(books, author);

        sc.close();
    }
}
