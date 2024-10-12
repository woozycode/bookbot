def main():
    def read_book():
        with open("books/frankenstein.txt", "r") as f:
            text = f.read()
        return text

    def count_words():
        with open("books/frankenstein.txt", "r") as f:
            text = f.read()
        words = text.split()
        word_count = len(words)
        return word_count

    def count_characters():
        character_dict = {}
        with open("books/frankenstein.txt", "r") as f:
            text = f.read()
        words = text.split()
        for word in words:
            for character in word:
                character = character.lower()
                if character not in character_dict:
                    character_dict.update({character: 1})
                elif character in character_dict:
                    character_dict.update({character: character_dict[character] + 1})
        return character_dict

    def run_report():
        word_count = count_words()
        character_dict = count_characters()

        character_dict_list = []
        for k, v in character_dict.items():
            sub_dict = {}
            sub_dict.update({"character": k})
            sub_dict.update({"occurences": v})
            character_dict_list.append(sub_dict)

        def sort_on(dict):
            return dict["occurences"]

        character_dict_list.sort(reverse=True, key=sort_on)

        report_str = ""
        for each_dict in character_dict_list:
            character_str = f"The '{each_dict['character']}' character was found {each_dict['occurences']} times\n"
            report_str = report_str + character_str

        print(
            f"""
--- Begin report of books/frankenstein.txt ---
{word_count} words found in the document 

{report_str}
"""
        )
        return

    print(count_words())

    print(count_characters())

    run_report()


if __name__ == "__main__":
    main()
