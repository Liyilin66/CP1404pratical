import wikipedia


def search_wikipedia():
    title = input("Enter page title: ")
    while title:
        try:
            # Attempt to fetch the page
            page = wikipedia.page(title, autosuggest=False)
            print(f"{page.title}\n{page.summary[:1000]}...\n{page.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An error occurred: {e}")

        title = input("Enter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    search_wikipedia()
