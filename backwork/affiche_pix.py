from backwork.Item import*

def affiche_pixels(toile, FPS, pixels, x, y, cam, plan): #certifié
    cam.place()
    for i in pixels:
        i.position(FPS)
    for i in  plan:
        i.dist(cam.x, cam.y, cam.z)
    plan = devant(plan)
    for p in plan:
        pixels[p.i].pers(x,y,cam.x, cam.y, cam.z, cam.d, cam.v)
        pixels[p.i].affiche(p)
    toile.update()
