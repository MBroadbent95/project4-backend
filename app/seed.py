from app import app, db
from models.recipe import RecipeModel
from models.comment import CommentModel
from models.user import UserModel

with app.app_context():

    try:
        print("Connected to our database")

        db.drop_all()

        db.create_all()

        nick = UserModel(
            username="Nick",
            email="nick@nick.com",
            password="meditate",
        )

        iury = UserModel(
            username="Iury",
            email="iury@iury.com",
            password="whataredreams",
        )
        db.session.add(nick)
        db.session.add(iury)
        db.session.commit()

        thai_green_curry = RecipeModel(
            name="Thai Green Curry",
            cuisine="Thai",
            serving="6 servings",
            prep_time="10 mins",
            total_time="40 mins",
            cal_serv=257,
            ingredients="225g new potatoes, cut into chunks, 100g green beans, trimmed and halved, 1 tbsp vegetable or sunflower oil, 1 garlic clove, chopped, 1 rounded tbsp or 4 tsp Thai green curry paste (you can't fit the tablespoon into some of the jars), 400ml can coconut milk, 2 tsp Thai fish sauce, 1 tsp caster sugar, 450g boneless skinless chicken (breasts or thighs), cut into bite-size pieces, 2 lime leaves finely shredded, or 3 wide strips lime zest, plus extra to garnish, good handful of basil leaves, boiled rice, to serve",
            directions_instructions="STEP 1 Put 225g new potatoes, cut into chunks, in a pan of boiling water and cook for 5 minutes. STEP 2 Add 100g trimmed and halved green beans and cook for a further 3 minutes, by which time both should be just tender but not too soft. Drain and put to one side. STEP 3 In a wok or large frying pan, heat 1 tbsp vegetable or sunflower oil until very hot, then drop in 1 chopped garlic clove and cook until golden, this should take only a few seconds. Don’t let it go very dark or it will spoil the taste. STEP 4 Spoon in 1 rounded tbsp Thai green curry paste and stir it around for a few seconds to begin to cook the spices and release all the flavours. STEP 5 Next, pour in a 400ml can of coconut milk and let it come to a bubble. STEP 6 Stir in 2 tsp Thai fish sauce and 1 tsp caster sugar, then 450g bite-size chicken pieces. Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked. STEP 7 Tip in the potatoes and beans and let them warm through in the hot coconut milk, then add 2 finely shredded lime leaves (or 3 wide strips lime zest). STEP 8 Add a good handful basil leaves, but only leave them briefly on the heat or they will quickly lose their brightness. STEP 9 Scatter with lime to garnish and serve immediately with boiled rice.",
            image_url="https://i.imgur.com/mdkcaBa.jpg",
            user_id=nick.id,
        )

        kung_pao_chicken_meatballs = RecipeModel(
            name="Kung Pao Chicken Meatballs",
            cuisine="Chinese",
            serving="4 servings",
            prep_time="20 mins",
            total_time="1 hr",
            cal_serv=419,
            ingredients="FOR MEATBALLS: 1 lb. ground chicken 2 cloves garlic, minced 2 tsp. fresh ginger, minced 2 green onions, thinly sliced  3/4 c. panko bread crumbs 1 large egg, beaten 1 tbsp. low-sodium soy sauce Kosher salt Freshly ground Szechuan peppercorns 2 tbsp. vegetable oil. FOR SAUCE: 1/2 c. low-sodium chicken broth 1/4 c. low-sodium soy sauce 2 tbsp. chinese cooking wine or dry sherry 2 tbsp. rice vinegar 1 tbsp. hoisin sauce 1 tbsp. granulated sugar 1 tbsp. cornstarch 2 bell peppers, chopped 10 dried red chilis 4 green onions, cut into 1 inch pieces  2 tsp. freshly minced ginger 2 cloves garlic, minced 1 1/2 tsp. freshly ground Szechuan peppercorns Roasted unsalted peanuts, for garnish Cooked white rice, for serving",
            directions_instructions="Step 1 In a medium bowl, combine ground chicken, garlic, ginger, green onions, and panko. Add egg and soy sauce and season with salt and few good cranks of pepper. Mix until well combined. Form into 16 equal sized meatballs. If mixture is too wet you can wet your hands lightly with water to help roll into balls. Step 2 In a large skillet over medium heat, heat oil. Add meatballs and cook until golden on all sides and internal temperature reaches 165°, 18 to 20 minutes. Remove from skillet and place on a plate to keep warm. Step 3 Meanwhile, in a small bowl, combine broth, soy sauce, cooking wine, vinegar, hoisin, and sugar. Add cornstarch and whisk until dissolved. Step 4 Wipe out any bits from skillet that are too dark. Return skillet over medium heat and add more oil as needed. Add bell peppers and cook until soft, 5 minutes. Add dried chilis, green onions, ginger, garlic, and pepper. Cook until fragrant, 2 minutes more. Add sauce mixture and return meatballs to skillet. Toss to coat meatballs. Reduce heat to a simmer and simmer until sauce is thickened and meatballs are warmed through, 5 minutes. Step 5 Top with peanuts and serve over rice.",
            image_url="https://i.imgur.com/NrkL76P.jpeg",
            user_id=iury.id,
        )

        burnt_aubergine_veggie_chilli = RecipeModel(
            name="Burnt Aubergine Veggie Chilli",
            cuisine="Mexican",
            serving="4 servings",
            prep_time="25 mins",
            total_time="2 hrs 25 mins",
            cal_serv=316,
            ingredients="1 aubergine, 1 tbsp olive oil or rapeseed oil, 1 red onion: diced, 2 carrots: finely diced, 70g puy lentils or green lentils: rinsed, 30g red lentils: rinsed, 400g can kidney beans, 3 tbsp dark soy sauce, 400g can chopped tomatoes, 20g dark chocolate: finely chopped, ¼ tsp chilli powder, 2 tsp dried oregano, 2 tsp ground cumin, 2 tsp sweet smoked paprika, 1 tsp coriander, 1 tsp cinnamon, 800ml vegetable stock, ½ lime juiced, To serve: brown rice, tortilla chips, mashed avocado, yogurt or soured cream, grated cheddar, roughly chopped coriander (optional)",
            directions_instructions="STEP 1 If you have a gas hob, put the aubergine directly onto a lit ring to char completely, turning occasionally with kitchen tongs, until burnt all over. Alternatively, use a barbecue or heat the grill to its highest setting and cook, turning occasionally, until completely blackened (the grill won’t give you the same smoky flavour). Set aside to cool on a plate, then peel off the charred skin and remove the stem. Roughly chop the flesh and set aside. STEP 2 In a large pan, heat the oil, add the onion and carrots with a pinch of salt, and fry over a low-medium heat for 15-20 mins until the carrots have softened. STEP 3 Add the aubergine, both types of lentils, the kidney beans with the liquid from the can, soy sauce, tomatoes, chocolate, chilli powder, oregano and the spices. Stir to combine, then pour in the stock. Bring to the boil, then turn down the heat to very low. Cover with a lid and cook for 1½ hrs, checking and stirring every 15-20 mins to prevent it from burning. STEP 4 Remove the lid and let the mixture simmer over a low-medium heat, stirring occasionally, for about 15 mins until you get a thick sauce. Stir in the lime juice and taste for seasoning – add more salt if needed. Serve hot over rice with whichever accompaniments you want!",
            image_url="https://i.imgur.com/L7nAYgg.jpeg",
            user_id=iury.id,
        )

        pasta_alla_vodka = RecipeModel(
            name="Pasta Alla Vodka",
            cuisine="Italian",
            serving="2 servings",
            prep_time="5 mins",
            total_time="30 mins",
            cal_serv=866,
            ingredients="2 tbsp olive oil, 1 banana shallot or ½ onion: finely chopped, 3 garlic cloves: crushed, ¼ tsp chilli flakes, 100g tomato purée, 5 tbsp vodka, 100ml double cream, 200g penne or rigatoni pasta, 30g grated parmesan or vegetarian alternative: plus extra to serve, small handful of basil leaves: to serve",
            directions_instructions="STEP 1 Heat the oil in a large frying pan or casserole dish. Add the shallot and a large pinch of salt and gently fry over a low heat for 10 mins or until softened and translucent. Add the garlic and chilli flakes and cook for 30 seconds. Stir through the tomato purée, cook for 2 mins, then stir through the vodka and cook for 3 mins. Quickly stir through the cream to combine, then remove from the heat. STEP 2 Cook the pasta in salted water following pack instructions. Drain and reserve 150ml cooking water. Add roughly 50ml of the water to the tomato sauce, then tip in the pasta and cheese, tossing everything together over a low heat until well coated and glossy (loosen with a splash more of the cooking water if it’s a little dry). Season to taste, then serve with a sprinkling of the extra parmesan, a good grinding of black pepper and the basil leaves scattered over the top.",
            image_url="https://i.imgur.com/tE1JmSQ.png",
            user_id=nick.id,
        )

        chilli_con_carne = RecipeModel(
            name="Chilli Con Carne",
            cuisine="Mexican",
            serving="4 servings",
            prep_time="10 mins",
            total_time="1 hr 10 mins",
            cal_serv=387,
            ingredients="1 large onion, 1 red pepper, 2 garlic cloves, 1 tbsp oil, 1 heaped tsp hot chilli powder (or 1 level tbsp if you only have mild), 1 tsp paprika, 1 tsp ground cumin, 500g lean minced beef, 1 beef stock cube, 400g can chopped tomatoes, ½ tsp dried marjoram, 1 tsp sugar (or add a thumbnail-sized piece of dark chocolate along with the beans instead, see tip), 2 tbsp tomato purée, 410g can red kidney beans, plain boiled long grain rice: to serve, soured cream: to serve",
            directions_instructions="STEP 1 Prepare your vegetables. Chop 1 large onion into small dice, about 5mm square. The easiest way to do this is to cut the onion in half from root to tip, peel it and slice each half into thick matchsticks lengthways, not quite cutting all the way to the root end so they are still held together. Slice across the matchsticks into neat dice. STEP 2 Cut 1 red pepper in half lengthways, remove stalk and wash the seeds away, then chop. Peel and finely chop 2 garlic cloves. STEP 3 Start cooking. Put your pan on the hob over a medium heat. Add 1 tbsp oil and leave it for 1-2 minutes until hot (a little longer for an electric hob). STEP 4 Add the onion and cook, stirring fairly frequently, for about 5 minutes, or until the onion is soft, squidgy and slightly translucent. STEP 5 Tip in the garlic, red pepper, 1 heaped tsp hot chilli powder or 1 level tbsp mild chilli powder, 1 tsp paprika and 1 tsp ground cumin. STEP 6 Give it a good stir, then leave it to cook for another 5 minutes, stirring occasionally. STEP 7 Brown 500g lean minced beef. Turn the heat up a bit, add the meat to the pan and break it up with your spoon or spatula. The mix should sizzle a bit when you add the mince. STEP 8 Keep stirring and prodding for at least 5 minutes, until all the mince is in uniform, mince-sized lumps and there are no more pink bits. Make sure you keep the heat hot enough for the meat to fry and become brown, rather than just stew. STEP 9 Make the sauce. Crumble 1 beef stock cube into 300ml hot water. Pour this into the pan with the mince mixture. STEP 10 Add a 400g can of chopped tomatoes. Tip in ½ tsp dried marjoram, 1 tsp sugar and add a good shake of salt and pepper. Squirt in about 2 tbsp tomato purée and stir the sauce well. STEP 11 Simmer it gently. Bring the whole thing to the boil, give it a good stir and put a lid on the pan. Turn down the heat until it is gently bubbling and leave it for 20 minutes. STEP 12 Check on the pan occasionally to stir it and make sure the sauce doesn’t catch on the bottom of the pan or isn’t drying out. If it is, add a couple of tablespoons of water and make sure that the heat really is low enough. After simmering gently, the saucy mince mixture should look thick, moist and juicy. STEP 13 Drain and rinse a 410g can of red kidney beans in a sieve and stir them into the chilli pot. Bring to the boil again, and gently bubble without the lid for another 10 minutes, adding a little more water if it looks too dry. STEP 14 Taste a bit of the chilli and season. It will probably take a lot more seasoning than you think. STEP 15 Now replace the lid, turn off the heat and leave your chilli to stand for 10 minutes before serving. This is really important as it allows the flavours to mingle. STEP 16 Serve with soured cream and plain boiled long grain rice.",
            image_url="https://i.imgur.com/a2ETDEM.jpeg",
            user_id=nick.id,
        )

        chicken_and_chorizo_jambalaya = RecipeModel(
            name="Chicken & Chorizo Jambalaya",
            cuisine="Cajun",
            serving="4 servings",
            prep_time="10 mins",
            total_time="55 mins",
            cal_serv=445,
            ingredients="1 tbsp olive oil, 2 chicken breasts: chopped, 1 onion: diced, 1 red pepper: thinly sliced, 2 garlic cloves: crushed, 75g chorizo: sliced, 1 tbsp Cajun seasoning, 250g long grain rice, 400g can plum tomato, 350ml chicken stock",
            directions_instructions="STEP 1 Heat 1 tbsp olive oil in a large frying pan with a lid and brown 2 chopped chicken breasts for 5-8 mins until golden. STEP 2 Remove and set aside. Tip in the 1 diced onion and cook for 3-4 mins until soft. STEP 3 Add 1 thinly sliced red pepper, 2 crushed garlic cloves, 75g sliced chorizo and 1 tbsp Cajun seasoning, and cook for 5 mins more. STEP 4 Stir the chicken back in with 250g long grain rice, add the 400g can of tomatoes and 350ml chicken stock. Cover and simmer for 20-25 mins until the rice is tender.",
            image_url="https://i.imgur.com/yxFyFsW.jpeg",
            user_id=iury.id,
        )

        spaghetti_bolognese = RecipeModel(
            name="Spaghetti Bolognese",
            cuisine="Italian",
            serving="6 servings",
            prep_time="25 mins",
            total_time="2 hrs 15 mins",
            cal_serv=624,
            ingredients="1 tbsp olive oil, 4 rashers smoked streaky bacon: finely chopped, 2 medium onions: finely chopped, 2 carrots: trimmed and finely chopped, 2 celery sticks: finely chopped, 2 garlic cloves: finely chopped, 2-3 sprigs rosemary leaves: picked and finely chopped, 500g beef mince. For the bolognese sauce, 2 x 400g tins plum tomatoes, small pack basil leaves picked: ¾ finely chopped and the rest left whole for garnish, 1 tsp dried oregano, 2 fresh bay leaves, 2 tbsp tomato purée, 1 beef stock cube, 1 red chilli deseeded and finely chopped (optional), 125ml red wine, 6 cherry tomatoes sliced in half: To season and serve, 75g parmesan grated: plus extra to serve, 400g spaghetti, crusty bread to serve (optional)",
            directions_instructions="STEP 1 Put a large saucepan on a medium heat and add 1 tbsp olive oil. STEP 2 Add 4 finely chopped bacon rashers and fry for 10 mins until golden and crisp. STEP 3 Reduce the heat and add the 2 onions, 2 carrots, 2 celery sticks, 2 garlic cloves and the leaves from 2-3 sprigs rosemary, all finely chopped, then fry for 10 mins. Stir the veg often until it softens. STEP 4 Increase the heat to medium-high, add 500g beef mince and cook stirring for 3-4 mins until the meat is browned all over. STEP 5 Add 2 tins plum tomatoes, the finely chopped leaves from ¾ small pack basil, 1 tsp dried oregano, 2 bay leaves, 2 tbsp tomato purée, 1 beef stock cube, 1 deseeded and finely chopped red chilli (if using), 125ml red wine and 6 halved cherry tomatoes. Stir with a wooden spoon, breaking up the plum tomatoes. STEP 6 Bring to the boil, reduce to a gentle simmer and cover with a lid. Cook for 1 hr 15 mins stirring occasionally, until you have a rich, thick sauce. STEP 7 Add the 75g grated parmesan, check the seasoning and stir. STEP 8 When the bolognese is nearly finished, cook 400g spaghetti following the pack instructions. STEP 9 Drain the spaghetti and either stir into the bolognese sauce, or serve the sauce on top. Serve with more grated parmesan, the remaining basil leaves and crusty bread, if you like.",
            image_url="https://i.imgur.com/Cv4jRLV.jpeg",
            user_id=iury.id,
        )

        ultimate_chocolate_cake = RecipeModel(
            name="Ultimate Chocolate Cake",
            cuisine="Dessert",
            serving="Up to 14 Slices",
            prep_time="30 - 40 mins",
            total_time="2 hrs 10 mins",
            cal_serv=541,
            ingredients="For the chocolate cake, 200g dark chocolate (about 60 percent cocoa solids): chopped, 200g butter: cubed, 1 tbsp instant coffee granules, 85g self-raising flour, 85g plain flour, ¼ tsp bicarbonate of soda, 200g light muscovado sugar, 200g golden caster sugar, 25g cocoa powder, 3 medium eggs, 75ml buttermilk, 50g grated chocolate or 100g curls, to decorate. For the ganache, 200g dark chocolate (about 60 percent cocoa solids): chopped, 300ml double cream, 2 tbsp golden caster sugar",
            directions_instructions="STEP 1 Heat the oven to 160C/fan 140C/gas 3. Butter and line a 20cm round cake tin (7.5cm deep). STEP 2 Put 200g chopped dark chocolate in a medium pan with 200g butter. STEP 3 Mix 1 tbsp instant coffee granules into 125ml cold water and pour into the pan. STEP 4 Warm through over a low heat just until everything is melted – don’t overheat. Or melt in the microwave for about 5 minutes, stirring halfway through. STEP 5 Mix 85g self-raising flour, 85g plain flour, ¼ tsp bicarbonate of soda, 200g light muscovado sugar, 200g golden caster sugar and 25g cocoa powder, and squash out any lumps. STEP 6 Beat 3 medium eggs with 75ml buttermilk. STEP 7 Pour the melted chocolate mixture and the egg mixture into the flour mixture and stir everything to a smooth, quite runny consistency. STEP 8 Pour this into the tin and bake for 1hr 25 – 1hr 30 mins. If you push a skewer into the centre it should come out clean and the top should feel firm (don’t worry if it cracks a bit). STEP 9 Leave to cool in the tin (don’t worry if it dips slightly), then turn out onto a wire rack to cool completely. Cut the cold cake horizontally into three. STEP 10 To make the ganache, put 200g chopped dark chocolate in a bowl. Pour 300ml double cream into a pan, add 2 tbsp golden caster sugar and heat until it is about to boil. STEP 11 Take off the heat and pour it over the chocolate. Stir until the chocolate has melted and the mixture is smooth. Cool until it is a little thicker but still pourable. STEP 12 Sandwich the layers together with just a little of the ganache. Pour the rest over the cake letting it fall down the sides and smooth over any gaps with a palette knife. STEP 13 Decorate with 50g grated chocolate or 100g chocolate curls. The cake keeps moist and gooey for 3-4 days.",
            image_url="https://i.imgur.com/7TCCZP1.jpeg",
            user_id=iury.id,
        )

        db.session.add(thai_green_curry)
        db.session.add(kung_pao_chicken_meatballs)
        db.session.add(burnt_aubergine_veggie_chilli)
        db.session.add(pasta_alla_vodka)
        db.session.add(chilli_con_carne)
        db.session.add(chicken_and_chorizo_jambalaya)
        db.session.add(spaghetti_bolognese)
        db.session.add(ultimate_chocolate_cake)
        db.session.commit()

        comment = CommentModel(
            content="Amazing taste.", recipe_id=thai_green_curry.id, user_id=nick.id
        )

        other_comment = CommentModel(
            content="Is it Spicey?",
            recipe_id=kung_pao_chicken_meatballs.id,
            user_id=iury.id,
        )
        comment.save()
        other_comment.save()

        print("Seeding some data")

    except Exception as e:
        print(e)
