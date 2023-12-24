def extract_mbti_tags(html_contents):
        """
            Extracts MBTI tags from the given HTML contents and returns their tag IDs.

                Args:
                    html_contents (str): The HTML content in which to search for MBTI types.

                        Returns:
                            list: A list of tag IDs corresponding to the MBTI types found in the content.
                                """

                                    # Dictionary of MBTI types with their tag IDs
    mbti_dict = {
                                                "enfj": {"id": 57, "description": "Persuasive, Altruistic, Harmonious"},
                                                        "enfp": {"id": 53, "description": "Enthusiastic, Creative, Social"},
                                                                "entj": {"id": 58, "description": "Confident, Decisive, Leader"},
                                                                        "entp": {"id": 54, "description": "Inventive, Original, Argumentative"},
                                                                                "esfj": {"id": 56, "description": "Cooperative, Warm, Organized"},
                                                                                        "esfp": {"id": 52, "description": "Lively, Fun-loving, Adaptable"},
                                                                                                "estj": {"id": 55, "description": "Efficient, Practical, Leader"},
                                                                                                        "estp": {"id": 51, "description": "Energetic, Social, Realistic"},
                                                                                                                "infj": {"id": 45, "description": "Insightful, Idealistic, Creative"},
                                                                                                                        "infp": {"id": 49, "description": "Idealistic, Emotional, Creative"},
                                                                                                                                "intj": {"id": 46, "description": "Strategic, Independent, Innovative"},
                                                                                                                                        "intp": {"id": 50, "description": "Intellectual, Curious, Theoretical"},
                                                                                                                                                "isfj": {"id": 44, "description": "Caring, Loyal, Traditional"},
                                                                                                                                                        "isfp": {"id": 48, "description": "Artistic, Peaceful, Adventurous"},
                                                                                                                                                                "istj": {"id": 43, "description": "Responsible, Practical, Organized"},
                                                                                                                                                                        "istp": {"id": 47, "description": "Practical, Analytical, Curious"}
                                                                                                                                                                            }

                                                                                                                                                                                # Lowercase the HTML content for case-insensitive matching
                                       content_lower = html_contents.lower()

                                                                                                                                                                                        # Find MBTI types in the content and collect their tag IDs
                                                                                                                                                                                            tag_ids = [mbti_dict[mbti]["id"] for mbti in mbti_dict if mbti in content_lower]

                                                                                                                                                                                                return tag_ids
